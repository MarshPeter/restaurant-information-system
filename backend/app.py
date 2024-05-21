from logic.analytics_collector import AnalyticsCollector
from logic.order_creator import OrderCreator
from logic.order_mediator import OrderMediator
from logic.order_parser import OrderParser
from logic.order_notifier import OrderNotifier
from db.db_access import DBAccess

from flask import Flask

db_access = DBAccess()
analytics_collector = AnalyticsCollector(db_access=db_access)
order_creator = OrderCreator()
order_parser = OrderParser()
order_notifer = OrderNotifier()

order_mediator = OrderMediator(order_parser=order_parser, 
                                order_creator=order_creator,
                                order_notifier=order_notifer,
                                analytics_collector=analytics_collector)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/api/login/<username>/<password>")
def authenticate_user(username, password):
    db_access = DBAccess()
    db_access.connect()
    query = f"SELECT username FROM Account WHERE username='{username}' AND password='{password}'"
    return f"Hello, this is {username}, {password}"

# This is an example of how to add routes + how to use the currently configured shitty database code. IT WILL CHANGE DEFINITELY YEP. (but please don't use it, it will spam the tables with duplicate data)
# @app.route("/test4")
# def test():
#     db_access = DBAccess()
#     db_access.connect()
#     query = 'INSERT INTO TableSeating (TableNum, OccupiedStatus) VALUES (%s, %s)'
#     data_query = (2, 1)
#     db_access.make_query(query, data_query)

#     return {
#         "test": 1
#     }