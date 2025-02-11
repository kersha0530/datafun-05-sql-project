import sqlite3

def setup_database():
    """Creates the buzzline database and tables."""
    conn = sqlite3.connect("buzzline_db.sqlite")
    cursor = conn.cursor()

    # Run SQL scripts
    with open("sql_create/01_drop_tables.sql") as f:
        cursor.executescript(f.read())
    
    with open("sql_create/02_create_tables.sql") as f:
        cursor.executescript(f.read())

    with open("sql_create/03_insert_records.sql") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
