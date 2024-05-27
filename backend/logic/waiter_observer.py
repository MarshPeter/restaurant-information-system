from .order_observer import OrderObserver
from .orders.order import Order
from .orders.order_enumerators import InRestaurantOrderState

class WaiterObserver(OrderObserver):
    def __init__(self):
        self.current_orders: list[Order] = []

    def update(self, order: Order) -> None:
        # Check if the order already exists
        for existing_order in self.current_orders:
            if existing_order._order_number == order._order_number:
                # Update the existing order's state
                if order.get_state() == InRestaurantOrderState.COMPLETE:
                    self.current_orders.remove(existing_order)
                else:
                    existing_order._current_state = order.get_state()
                return
        # If the order is in the READYTOSERVE state, add it
        if order.get_state() == InRestaurantOrderState.READYTOSERVE:
            self.current_orders.append(order)

    def retrieve_orders(self) -> list[Order]:
        return self.current_orders