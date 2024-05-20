# util/db_property_util.py

class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        server_name = "DESKTOP-K702Q3Q\\SQLEXPRESS09"  # Note the double backslash for escaping
        database_name = "virtual_art_gallery"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return str(conn_str)  # Ensure the connection string is returned as a string

