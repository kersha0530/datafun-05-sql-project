import sqlite3
import pandas as pd

def execute_query(query):
    """Executes a given SQL query and returns the result."""
    conn = sqlite3.connect("buzzline_db.sqlite")
    cursor = conn.cursor()
    
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    return rows

def main():
    queries = {
        "Aggregation": "sql_queries/query_aggregation.sql",
        "Filter": "sql_queries/query_filter.sql",
        "Sorting": "sql_queries/query_sorting.sql",
        "Group By": "sql_queries/query_group_by.sql",
        "Join": "sql_queries/query_join.sql"
    }

    for name, path in queries.items():
        print(f"\n{name} Query Results:")
        with open(path, "r") as file:
            query = file.read()
            results = execute_query(query)
            df = pd.DataFrame(results)
            print(df)

if __name__ == "__main__":
    main()
