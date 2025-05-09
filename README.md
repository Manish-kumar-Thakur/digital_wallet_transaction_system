# digital_wallet_transaction_system

A CLI-based digital wallet system built in Python with MySQL integration. This application allows users to register, manage wallet balances, and perform transactions (send/receive funds) based on a tiered user system with transactions.



## Features

- User Registration with Tier Selection (Basic, Custom, Premium)
- Secure Password Management (Encapsulated)
- Wallet Creation & Balance Tracking
- Peer-to-Peer Money Transfer
- Transaction History
- MySQL Integration for Persistent Storage
-  Modular Codebase for Scalability and Maintenance



## Project Structure
```
Digital_Wallet_Transaction_System/
│
├── user.py              # User model, registration, database interaction
├── wallet.py            # Wallet operations (add, send, receive, fees)
├── transaction.py      # Transaction logging and model
├── db.py              # Database connection utility
├── main.py              # CLI entry point and flow control

```


## Tech Stack

- Language: Python 3.x
- Database: MySQL
- ORM/DB Access: Raw SQL with `mysql-connector-python`



## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Digital_Wallet_Transaction_System.git
cd Digital_Wallet_Transaction_System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

- Create a database named `wallet_db`
- Execute the provided SQL script (if any) to create tables:
  - `users`
  - `wallets`
  - `transactions`

### 4. Update Database Connection

Edit `dwts.py` with your MySQL credentials:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_password",
        database="wallet_db"
    )
```


## Running the Project

bash
python main.py



## User Tier Limits

| Tier     | 
|----------|
| Basic    | 
| Custom   | 
| Premium  | 



## Contributing

Contributions are welcome! Please fork the repo and open a pull request.



## License

This project is licensed under the MIT License.


## Contact
**Author**: [Manish Kumar Thakur]  
**Email**: mansihthakur.js@gmail.com
**GitHub**: [Manish-Kumar-Thakur](https://github.com/Manish-Kumar-Thakur)
