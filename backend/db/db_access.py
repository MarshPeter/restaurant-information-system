import mysql.connector

class DBAccess:
    def __init__(self):
        self._connection = None

    def connect(self):
        # use this to get your password details, this will just print it on the server when you connect
        print(os.environ.get('DB_PASSWORD'))
        if self._connection is None:
            # password=os.environ.get('DB_PASSWORD'),
            self._connection = mysql.connector.connect(
                host=os.environ.get("DB_HOST"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get('DB_PASSWORD'),
                database=os.environ.get('DATABASE')
            )

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
