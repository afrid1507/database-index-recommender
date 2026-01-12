import sqlite3
import time

def measure_query_time(query):
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()

    start = time.time()
    cursor.execute(query)
    cursor.fetchall()
    end = time.time()

    conn.close()
    return round(end - start, 6)
