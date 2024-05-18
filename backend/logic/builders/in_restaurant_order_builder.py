from .order_builder import OrderBuilder
from ..orders.in_restaurant_order import InRestaurantOrder

class InRestaurantOrderBuilder(OrderBuilder):

    _order: InRestaurantOrder
    _current_order_number: int

    def __init__(self):
        self._current_order_number = 1
        self.reset_order()

    def reset_order(self):
        self._order = InRestaurantOrder(self._current_order_number)
        self._increment_order_number()

    def add_menu_item(self, menu_item: dict):
        self._order.add_menu_item(menu_item)

    def set_customer(self, customer: str = "N/A"):
        self._order.set_customer(customer)

    def set_destination(self, location: str):
        self._order.set_location(location)

    def get_order(self):
        curr_order = self._order
        self.reset_order()
        return curr_order

    def _increment_order_number(self):
        self._current_order_number = self._current_order_number + 1

        if self._current_order_number >= 1000:
            self._current_order_number = 1
    