import os

def execute_sql_files(cursor, sql_file_path):
    try:
        # Read the SQL file
        with open(sql_file_path, 'r') as sql_file:
            sql_query = sql_file.read()

        # Execute the SQL query
        cursor.execute(sql_query)

        print(f"Query Executed Using {sql_file_path}.")

    except Exception as error:
        print(f"Error while executing {sql_file_path}:", error)
