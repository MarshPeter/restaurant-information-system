from .order_observer import OrderObserver

class KitchenObserver(OrderObserver):
    def __init__(self):
        self.current_orders = []

    def update(self, order):
        # Logic to update kitchen orders
        self.current_orders.append(order)
        print("I am currently in the observer")
        print(self.current_orders)

