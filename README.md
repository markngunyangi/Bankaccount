# Bank Account Project Interview(FastAPI, Python, HTML, CSS, JS)

## Prerequisites

Before running the project, ensure you have the following installed:

- Python (version 3.7 or higher)
- pip (Python package installer)
- A modern web browser

## Installation

1. Clone the repository to your local machine:

   
   git clone https://github.com/your-username/bank-account-project.git
  

2. Navigate to the project directory:

   
   cd bank-account-project
  

3. Install the required Python packages:

   
   pip install -r requirements.txt
   

## Running the Server

To start the server, run the following command:


uvicorn main:app --reload


This command will start the server locally, and it will automatically reload whenever you make changes to the code.

Once the server is running, you can access the web application by opening a web browser and navigating to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

1. **Checking Balance**: Upon accessing the web application, the current balance will be displayed.

2. **Depositing Money**: To deposit money into the account, enter the desired amount in the "Deposit" section and click the "Deposit" button. Follow the specified deposit limits.

3. **Withdrawing Money**: To withdraw money from the account, enter the desired amount in the "Withdraw" section and click the "Withdraw" button. Follow the specified withdrawal limits.

## API Endpoints

- `/balance`: GET request to retrieve the current balance.
- `/deposit`: POST request to deposit money into the account.
- `/withdraw`: POST request to withdraw money from the account.

## Testing

Once the server is running, open a web browser and navigate to http://127.0.0.1:8000/docs.

You'll see the FastAPI Swagger UI interface, which provides a comprehensive documentation of your API endpoints along with input fields to test each endpoint.
# Bankaccount
# Bankaccount
