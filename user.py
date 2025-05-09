from db import get_connection
from tabulate import tabulate

def register_user(name, phone, password, tier, limit_amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, phone, password, tier, limit_amount) VALUES (%s, %s, %s, %s, %s)",
        (name, phone, password, tier, limit_amount)
    )
    user_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO wallets (user_id, phone, balance) VALUES (%s, %s, %s)",
        (user_id, phone, 0.00)
    )
    conn.commit()
    conn.close()
    print("✅ User registered and wallet created.")

def view_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, tier, limit_amount FROM users")
    users = cursor.fetchall()
    print(tabulate(users, headers=["ID", "Name", "Phone", "Tier", "Limit"], tablefmt="psql"))
    conn.close()
