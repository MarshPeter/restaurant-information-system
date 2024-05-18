from .order_builder import OrderBuilder
from ..orders.takeaway_order import TakeawayOrder

class TakeawayOrderBuilder(OrderBuilder):
    _order: TakeawayOrder
    _current_order_number: int

    def __init__(self):
        self._current_order_number = 2001
        self.reset_order()
        
    def reset_order(self):
        self._order = TakeawayOrder(self._current_order_number)
        self._increment_order_number()

    def add_menu_item(self, menu_item: dict):
        self._order.add_menu_item(menu_item)

    def set_customer(self, customer: str = "N/A"):
        self._order.set_customer(customer)

    def set_destination(self, location: str):
        pass

    def get_order(self):
        curr_order = self._order
        self.reset_order()
        return curr_order

    def _increment_order_number(self):
        self._current_order_number = self._current_order_number + 1

        if self._current_order_number >= 3000:
            self._currentNumber = 1