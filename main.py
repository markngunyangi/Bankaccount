from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

app = FastAPI()



# transactions model
class Transaction(BaseModel):
    amount: float


max_deposit_amount = 150000
max_deposit_frequency = 4
max_withdrawal_amount = 50000
max_withdrawal_frequency = 3

current_date = datetime.now().date()
deposit_count = 0
withdrawal_count = 0
deposit_total = 0
withdrawal_total = 0

#Test api
@app.get("/test")
def read_root():
    return {"Hello": "World"}


# balance
@app.get("/balance")
def get_balance():
    return {"balance": deposit_total - withdrawal_total}

# deposit money
@app.post("/deposit")
def deposit_money(transaction: Transaction):
    global deposit_count, deposit_total, current_date
    
    if current_date != datetime.now().date():
        current_date = datetime.now().date()
        deposit_count = 0
        deposit_total = 0
    
    if deposit_count >= max_deposit_frequency:
        raise HTTPException(status_code=400, detail="Exceeded Maximum Deposit Frequency")
    
    if transaction.amount > max_deposit_amount:
        raise HTTPException(status_code=400, detail="Exceeded Maximum Deposit Per Transaction")
    
    if deposit_total + transaction.amount > max_deposit_amount:
        raise HTTPException(status_code=400, detail="Exceeded Maximum Deposit for the Day")
    
    deposit_count += 1
    deposit_total += transaction.amount
    return {"message": "Deposit successful"}

# withdraw money
@app.post("/withdraw")
def withdraw_money(transaction: Transaction):
    global withdrawal_count, withdrawal_total, current_date
    
    if current_date != datetime.now().date():
        current_date = datetime.now().date()
        withdrawal_count = 0
        withdrawal_total = 0
    
    if withdrawal_count >= max_withdrawal_frequency:
        raise HTTPException(status_code=400, detail="Exceeded Maximum Withdrawal Frequency")
    
    if transaction.amount > max_withdrawal_amount:
        raise HTTPException(status_code=400, detail="Exceeded Maximum Withdrawal Per Transaction")
    
    if transaction.amount > deposit_total - withdrawal_total:
        raise HTTPException(status_code=400, detail="Insufficient Balance")
    
    withdrawal_count += 1
    withdrawal_total += transaction.amount
    return {"message": "Withdrawal successful"}

# serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("frontend/index.html", "r") as f:
        return f.read()

app.mount("/static", StaticFiles(directory="frontend"), name="static")
