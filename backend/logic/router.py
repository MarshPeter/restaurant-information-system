from order_notifier import OrderNotifier
from kitchen_observer import KitchenObserver
from waiter_observer import WaiterObserver

class Router:
    def __init__(self):
        self.order_notifier = OrderNotifier()
        self.kitchen_observer = KitchenObserver()
        self.waiter_observer = WaiterObserver()

        self.order_notifier.subscribe('kitchen', self.kitchen_observer)
        self.order_notifier.subscribe('waiter', self.waiter_observer)

    def update_order(self, order_number):
        # Logic to determine order and notify observers
        order = {"number": order_number, "status": "updated"}
        self.order_notifier.notify('kitchen', order)
        self.order_notifier.notify('waiter', order)

    def retrieve_kitchen_orders(self):
        return self.kitchen_observer.current_orders

    def retrieve_waiter_orders(self):
        return self.waiter_observer.current_orders
