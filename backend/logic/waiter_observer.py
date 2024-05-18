from order_observer import OrderObserver

class WaiterObserver(OrderObserver):
    def __init__(self):
        self.current_orders = []

    def update(self, order):
        # Logic to update waiter orders
        self.current_orders.append(order)
