import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    order_date TEXT,
    amount REAL
)
""")

for _ in range(50000):
    cursor.execute("""
    INSERT INTO orders (customer_id, product_id, order_date, amount)
    VALUES (?, ?, ?, ?)
    """, (
        random.randint(1, 1000),
        random.randint(1, 100),
        (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        round(random.uniform(100, 5000), 2)
    ))

conn.commit()
conn.close()

print("Database created successfully")
