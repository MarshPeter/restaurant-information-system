from .order_observer import OrderObserver
from .orders.order import Order
from .orders.order_enumerators import InRestaurantOrderState

class KitchenObserver(OrderObserver):
    def __init__(self):
        self.current_orders: list[Order] = []

    def update(self, order: Order) -> None:
        # Check if the order already exists
        for existing_order in self.current_orders:
            if existing_order._order_number == order._order_number:
                # Update the existing order's state
                if order.get_state() == InRestaurantOrderState.READYTOSERVE:
                    self.current_orders.remove(existing_order)
                else:
                    existing_order._current_state = order.get_state()
                return
        # If the order does not exist and is not ready to serve, add it
        if order.get_state() != InRestaurantOrderState.READYTOSERVE:
            self.current_orders.append(order)
    
    def retrieve_orders(self) -> list[Order]:
        return self.current_orders

    def get_and_remove_order(self, order_number) -> Order:
        for order in self.current_orders:
            if order._order_number == order_number:
                self.current_orders.remove(order)
                return order
        return None
