import os
from database.connection import get_db_connection, close_db_connection
from etl.execute import execute_sql_files
from etl.insert import insert_json_data

# Directory containing SQL files for table creation before data insertion
sql_directory_before_insert = 'raw_schema'

# List of directories containing SQL files for table creation after data insertion
sql_directories_after_insert = ['std/create', 'std/insert']

# Replace 'path_to_your_directory' with the actual path to the directory containing your JSON files
directory_path = 'data'

# Initializing custom database connection for each JSON file insertion
connection = get_db_connection()

# Reading and executing SQL files to create tables (before data insertion)
for filename in os.listdir(sql_directory_before_insert):
    if filename.endswith(".sql"):
        sql_file_path = os.path.join(sql_directory_before_insert, filename)
        execute_sql_files(connection.cursor(), sql_file_path)

# Iterating through each file in the directory for JSON data insertion
for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        json_file_path = os.path.join(directory_path, filename)

        
        table_name = os.path.splitext(os.path.basename(json_file_path))[0]

        
        schema_name = 'raw'

        # Inserting data from JSON file into its respective table
        insert_json_data(json_file_path, connection, schema_name, table_name)

# Commiting the data insertion changes to the database before executing other SQL files
connection.commit()

# Reading and executing  SQL files from multiple directories (after data insertion)
for sql_directory in sql_directories_after_insert:
    if os.path.exists(sql_directory) and os.path.isdir(sql_directory):
        # Fetching the list of SQL files in the directory and sort them if necessary
        sql_files = sorted(filename for filename in os.listdir(sql_directory) if filename.endswith(".sql"))

        for filename in sql_files:
            sql_file_path = os.path.join(sql_directory, filename)
            execute_sql_files(connection.cursor(), sql_file_path)
    else:
        print(f"Directory '{sql_directory}' does not exist or is not a directory.")

connection.commit()
# Closing the connection
close_db_connection(connection)

print("All data inserted and SQL execution completed successfully. Connection closed.")
