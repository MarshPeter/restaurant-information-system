import mysql.connector
import os

# This is not a singleton at this stage, just enough to get things working. I think?
class DBAccess:

    _connection = None

    # this is probably bug ridden - good luck!
    def connect(self):
        # use this to get your password details, this will just print it on the server when you connect
        print(os.environ.get('DB_PASSWORD'))
        if self._connection is None:
            # password=os.environ.get('DB_PASSWORD'),
            self._connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Gavegave1*",
                database="information_system"
            )

    def disconnect(self):
        if self._connection is not None:
            self._connection.close()

    # use this if doing complicated queries
    def retrieve_connection(self):
        return self._connection

    # This is just to showcase how it works, probably needs to be redone at some point
    def make_query(self, query, values):
        print("TESTING")
        result = None
        try:
            cursor = self._connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
            cursor.close()
            self.disconnect()
        except Exception as err:
            print(err)

        return result

        # following is old code that probably needs to be in an insert method
        # try:
        #     cursor = self._connection.cursor()
        #     cursor.execute(query, values)
        #     cursor.close()
        #     self.disconnect()
        # except Exception as err:
        #     print(err)

