import json
from psycopg2.extras import Json

def insert_json_data(json_file_path, connection, schema_name, table_name):
    try:
        # Open a cursor to perform database operations
        cursor = connection.cursor()

        # Read the JSON file line by line and parse each line individually
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            for line in json_file:
                json_data = json.loads(line)

                # Prepare and execute the SQL query to insert data into the table
                columns = ', '.join(json_data.keys())
                placeholders = ', '.join(['%s'] * len(json_data))
                values = tuple(Json(value) if isinstance(value, (dict, list)) else value for value in json_data.values())
                insert_query = f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({placeholders});"
                cursor.execute(insert_query, values)

        # Commit the changes to the database
        connection.commit()

        # Close the cursor
        cursor.close()

        print(f"Data from {json_file_path} inserted into table {schema_name}.{table_name} successfully!")

    except Exception as error:
        print(f"Error while inserting data from {json_file_path} into table {schema_name}.{table_name}:", error)
