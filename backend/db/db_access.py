import mysql.connector
import os

# This is not a singleton at this stage, just enough to get things working. I think?
class DBAccess:

    _connection = None

    # this is probably bug ridden - good luck!
    def connect(self):
        print(os.environ.get('DB_PASSWORD'))
        if self._connection is None:
            self._connection = mysql.connector.connect(
                host="feenix-mariadb.swin.edu.au",
                user="s102573805",
                password=os.environ.get('DB_PASSWORD'),
                database="s102573805_db"
            )

    def disconnect(self):
        if self._connection is not None:
            self._connection.close()

    # This is just to showcase how it works, probably needs to be redone at some point
    def make_query(self, query, values):
        print("TESTING")
        try:
            cursor = self._connection.cursor()
            cursor.execute(query, values)
            self._connection.commit()
            cursor.close()
            self.disconnect()
        except Exception as err:
            print(err)

