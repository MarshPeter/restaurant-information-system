from .order_observer import OrderObserver
from .orders.order import Order  

class WaiterObserver(OrderObserver):
    def __init__(self):
        self.current_orders: list[Order] = []

    def update(self, order: Order) -> None:
        order.advance_state()

    def retrieve_orders(self) -> list[Order]:
        return self.current_orders

    def add_order(self, order: Order) -> None:
        self.current_orders.append(order)
