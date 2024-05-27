from .orders.order import Order

class OrderNotifier:
    def __init__(self):
        self._observers = {}

    def subscribe(self, notify_type: str, observer):
        if notify_type not in self._observers:
            self._observers[notify_type] = []
        self._observers[notify_type].append(observer)

    def unsubscribe(self, notify_type: str, observer):
        if notify_type in self._observers:
            self._observers[notify_type].remove(observer)

    def send_notifications(self, notify_type: str, order: Order):
        print(order.get_details()["state"])
        if notify_type in self._observers:
            for observer in self._observers[notify_type]:
                observer.update(order)
