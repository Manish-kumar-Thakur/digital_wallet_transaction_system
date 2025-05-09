from db import get_connection
from tabulate import tabulate

def send_money(sender_phone, receiver_phone, amount, processor="INTERNAL"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM wallets WHERE phone = %s", (sender_phone,))
    sender = cursor.fetchone()

    cursor.execute("SELECT wallet_id FROM wallets WHERE phone = %s", (receiver_phone,))
    receiver = cursor.fetchone()

    if not sender or not receiver:
        print("Sender or receiver wallet not found.")
        conn.close()
        return

    if sender[0] < amount:
        print("Insufficient balance.")
        conn.close()
        return

    cursor.execute("UPDATE wallets SET balance = balance - %s WHERE phone = %s", (amount, sender_phone))
    cursor.execute("UPDATE wallets SET balance = balance + %s WHERE phone = %s", (amount, receiver_phone))

    cursor.execute("""
        INSERT INTO transactions (sender_phone, receiver_phone, amount, processor, status)
        VALUES (%s, %s, %s, %s, 'SUCCESS')
    """, (sender_phone, receiver_phone, amount, processor))

    conn.commit()
    conn.close()
    print("Transaction successful.")

def view_transactions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, sender_phone, receiver_phone, amount, status, created_at FROM transactions ORDER BY created_at DESC")
    txns = cursor.fetchall()
    print(tabulate(txns, headers=["ID", "Sender", "Receiver", "Amount", "Status", "Date"], tablefmt="psql"))
    conn.close()
