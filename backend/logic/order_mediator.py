from order_parser import OrderParser
from order_creator import OrderCreator
from order_notifier import OrderNotifier
from analytics_collector import AnalyticsCollector

class OrderMediator:

    def __init__(self, order_parser, order_creator, order_notifier, analytics_collector):
        self._order_parser = order_parser
        self._order_creator = order_creator
        self._order_notifier = order_notifier
        self._analytics_collector = analytics_collector
