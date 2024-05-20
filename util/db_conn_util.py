#db_conn_util.py
import pyodbc
from util import db_property_util

class DBConnection:
    def __init__(self):
        # Get the connection string from the property util class
        self.connection_string = db_property_util.DBPropertyUtil.get_connection_string()

    def connect(self):
        try:
            # Establish the connection
            conn = pyodbc.connect(self.connection_string)
            return conn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {str(e)}")
            return None

# Example usage:
if __name__ == "__main__":
    db_connection = DBConnection()
    conn = db_connection.connect()
    if conn:
        print("Connected to the database successfully.")
        # Perform database operations here
        conn.close()
