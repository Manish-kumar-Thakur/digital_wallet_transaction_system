from db import get_connection

def add_balance(phone, amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE wallets SET balance = balance + %s WHERE phone = %s", (amount, phone))
    conn.commit()
    conn.close()
    print("Balance added successfully.")

def check_balance(phone):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM wallets WHERE phone = %s", (phone,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(f"Current Balance: ${result[0]:.2f}")
    else:
        print("Wallet not found.")
