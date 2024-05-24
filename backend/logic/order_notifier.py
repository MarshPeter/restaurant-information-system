from typing import Dict, List
from .order_observer import OrderObserver
from .orders.order import Order

class OrderNotifier:
    def __init__(self):
        self.observers: Dict[str, List[OrderObserver]] = {}

    def subscribe(self, notify_type: str, observer: OrderObserver):
        if notify_type not in self.observers:
            self.observers[notify_type] = []
        self.observers[notify_type].append(observer)

    def unsubscribe(self, notify_type: str, observer: OrderObserver):
        if notify_type in self.observers:
            self.observers[notify_type].remove(observer)

    def send_notifications(self, notify_type: str, order:Order):
        if notify_type in self.observers:
            for observer in self.observers[notify_type]:
                observer.update(order)
