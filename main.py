import os
from database.connection import get_db_connection, close_db_connection
from etl.execute import execute_sql_files
from etl.insert import insert_json_data

# Directory containing SQL files for table creation before data insertion
sql_directory_before_insert = 'create'

# List of directories containing SQL files for table creation after data insertion
sql_directories_after_insert = ['fact/create', 'fact/insert']

# Replace 'path_to_your_directory' with the actual path to the directory containing your JSON files
directory_path = 'data'

# Initialize your custom database connection for each JSON file insertion
connection = get_db_connection()

# Read and execute SQL files to create tables (before data insertion)
for filename in os.listdir(sql_directory_before_insert):
    if filename.endswith(".sql"):
        sql_file_path = os.path.join(sql_directory_before_insert, filename)
        execute_sql_files(connection.cursor(), sql_file_path)

# Iterate through each file in the directory for JSON data insertion
for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        json_file_path = os.path.join(directory_path, filename)

        # Get the table name from the JSON file's name (without the .json extension)
        table_name = os.path.splitext(os.path.basename(json_file_path))[0]

        # Insert data from JSON file into its respective table
        insert_json_data(json_file_path, connection, table_name)

# Commit the data insertion changes to the database before executing other SQL files
connection.commit()

# Read and execute SQL files from multiple directories (after data insertion)
for sql_directory in sql_directories_after_insert:
    for filename in os.listdir(sql_directory):
        if filename.endswith(".sql"):
            sql_file_path = os.path.join(sql_directory, filename)
            execute_sql_files(connection.cursor(), sql_file_path)

# Close the connection
close_db_connection(connection)

print("All data inserted and SQL execution completed successfully. Connection closed.")
