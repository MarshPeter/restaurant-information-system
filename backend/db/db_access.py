import mysql.connector

class DBAccess:
    def __init__(self):
        self._connection = None

    def connect(self):
        if self._connection is None or not self._connection.is_connected():
            try:
                self._connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="swe"
                )
                print("Database connection established")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self._connection = None

    def disconnect(self):
        if self._connection is not None and self._connection.is_connected():
            self._connection.close()
            self._connection = None
            print("Database connection closed")

    def execute_query(self, query, values=None):
        self.connect()
        result = None
        try:
            cursor = self._connection.cursor()
            cursor.execute(query, values)
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
            else:
                self._connection.commit()
                result = cursor.lastrowid
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Query error: {err}")
        finally:
            self.disconnect()
        return result
