import sqlite3
from datetime import datetime

DB_NAME = "project_delta.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS change_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            change_text TEXT,
            environment TEXT,
            rollback_plan TEXT,
            risk TEXT,
            cab_decision TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_change_request(change_text, environment, rollback_plan, risk, cab_decision):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO change_requests 
        (change_text, environment, rollback_plan, risk, cab_decision, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        change_text,
        environment,
        rollback_plan,
        risk,
        cab_decision,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_all_change_requests():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, environment, risk, cab_decision, created_at 
        FROM change_requests 
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
