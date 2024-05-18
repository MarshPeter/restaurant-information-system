from .order import Order
from .order_enumerators import InRestaurantOrderState

class InRestaurantOrder(Order):

    _current_state: InRestaurantOrderState
    _table: str
    _customer: str

    def __init__(self, order_number: int):
        super().__init__(order_number=order_number)
        self._current_state = InRestaurantOrderState.LOGGING

    def advance_state(self):
        _current_state = InRestaurantOrderState(_current_state + 1)

    def get_state(self):
        return self._current_state

    def set_customer(self, customer: str):
        self._customer = customer
    
    def set_location(self, location: str):
        self._table = "Table: " + location

    def get_details(self):
        dict_details = {
            "type": "in_restaurant",
            "order_number": self._order_number,
            "table": self._table,
            "customer": self._customer,
            "menu_items": self._menu_items
        }

        return dict_details