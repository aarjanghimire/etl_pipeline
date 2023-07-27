import os
import psycopg2
from dotenv import load_dotenv

def get_db_connection():
    try:
        # Load the environment variables from the .env file
        load_dotenv()

        # Get the database credentials from environment variables
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")

        # Build the database connection string
        db_connection_parameters = f"dbname={db_name} user={db_user} password={db_password} host={db_host}"
        connection = psycopg2.connect(db_connection_parameters)

        print("Database connection successful!")
        return connection

    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        raise


def close_db_connection(connection):
    try:
        connection.close()
        print("Database connection closed successfully!")

    except Exception as e:
        print(f"Error: Unable to close the database connection - {e}")
        raise
