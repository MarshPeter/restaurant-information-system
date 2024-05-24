from .order_observer import OrderObserver
from .orders.order import Order

class KitchenObserver(OrderObserver):
    def __init__(self):
        self.current_orders: list[Order] = []

    def update(self, order) -> None:
        self.current_orders.append(order)
    
    def retrieve_orders(self) -> list[Order]:
        return self.current_orders

    def get_and_remove_order(self, order_number) -> Order: 
        for order in self.current_orders:
            order_details = order.get_details()
            if order_details["order_number"] == order_number:
                return order
