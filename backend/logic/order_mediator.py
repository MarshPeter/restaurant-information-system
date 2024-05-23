from .order_parser import OrderParser
from .order_notifier import OrderNotifier
from .analytics_collector import AnalyticsCollector
class OrderMediator:

    def __init__(self, order_parser, order_creator, order_notifier, analytics_collector):
        self._order_parser = order_parser
        self._order_creator = order_creator
        self._order_notifier = order_notifier
        self._analytics_collector = analytics_collector

    def notify(self, order, next_step):
        if next_step == "analyse":
            # send to analyticsCollector
            pass
        if next_step == "send alerts":
            # send to order Notifier
            pass

    def create_order(self, order_dict) -> None:
        self._order_parser.create_order(order_dict)
