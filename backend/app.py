from logic.analytics_collector import AnalyticsCollector
from logic.order_creator import OrderCreator
from logic.order_mediator import OrderMediator
from logic.order_parser import OrderParser
from logic.order_notifier import OrderNotifier

from flask import Flask

analytics_collector = AnalyticsCollector()
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

