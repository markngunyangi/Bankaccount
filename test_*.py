import pytest
import requests


BASE_URL = "http://127.0.0.1:8000" 


def test_balance():
    response = requests.get(f"{BASE_URL}/balance")
    assert response.status_code == 200
    assert "balance" in response.json()


def test_deposit():
    data = {"amount": 10000}  
    response = requests.post(f"{BASE_URL}/deposit", json=data)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Deposit successful"


def test_withdraw():
    data = {"amount": 5000}  
    response = requests.post(f"{BASE_URL}/withdraw", json=data)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Withdrawal successful"


def test_max_deposit_amount():
    data = {"amount": 200000} 
    response = requests.post(f"{BASE_URL}/deposit", json=data)
    assert response.status_code == 400
    assert "detail" in response.json()
    assert response.json()["detail"] == "Exceeded Maximum Deposit Per Transaction"



