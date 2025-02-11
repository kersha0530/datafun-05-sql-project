"""
utils_db.py

This module contains helper functions for interacting with the SQLite database.
"""

import sqlite3
import os

def connect_to_db(db_name="buzzline_db.sqlite"):
    """Connect to SQLite database (or create if it doesn't exist)."""
    return sqlite3.connect(db_name)

def execute_query(connection, query, parameters=()):
    """Execute a SQL query with optional parameters."""
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()

def fetch_all(connection, query, parameters=()):
    """Execute a query and return all results."""
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    return cursor.fetchall()

if __name__ == "__main__":
    print("Database utilities module loaded.")
