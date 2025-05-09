import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pindecode@2026",
        database="digital_wallet_transaction_system"
    )
