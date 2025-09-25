import sqlite3
import os
from datetime import datetime, timedelta

DB_FILE = 'sample_data.db'

def create_db():
    # Remove the old database file if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create 'sprints' table
    cursor.execute('''
    CREATE TABLE sprints (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        story_points INTEGER NOT NULL
    )
    ''')

    # Create 'expenses' table
    cursor.execute('''
    CREATE TABLE expenses (
        id INTEGER PRIMARY KEY,
        item TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
    ''')

    # Insert sample data into 'sprints'
    sprints_data = [
        ('Sprint 1', 25),
        ('Sprint 2', 30),
        ('Sprint 3', 28)
    ]
    cursor.executemany('INSERT INTO sprints (name, story_points) VALUES (?, ?)', sprints_data)

    # Insert sample data into 'expenses'
    expenses_data = [
        ('Office Rent', 'Utilities', 1500.00, datetime.now().strftime('%Y-%m-%d')),
        ('New Server', 'Hardware', 2500.50, (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')),
        ('Software Licenses', 'Software', 350.00, (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')),
        ('Team Lunch', 'Food', 150.75, (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')),
        ('Cloud Services', 'Utilities', 800.00, (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')),
        ('Keyboard', 'Hardware', 99.99, (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')),
        ('Project Management Tool', 'Software', 120.00, (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')),
        # Previous month's data
        ('Old Invoice', 'Utilities', 1400.00, (datetime.now() - timedelta(days=35)).strftime('%Y-%m-%d')),
    ]
    cursor.executemany('INSERT INTO expenses (item, category, amount, date) VALUES (?, ?, ?, ?)', expenses_data)

    conn.commit()
    conn.close()
    print(f"Database '{DB_FILE}' created successfully with sample data.")

if __name__ == '__main__':
    create_db()