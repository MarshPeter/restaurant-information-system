from .order import Order
from .order_enumerators import InRestaurantOrderState

class InRestaurantOrder(Order):

    _current_state: InRestaurantOrderState
    _table: str
    _customer: str

    def __init__(self, order_number: int) -> None:
        super().__init__(order_number=order_number)
        self._current_state = InRestaurantOrderState.LOGGING

    def advance_state(self) -> None:
        if self._current_state == InRestaurantOrderState.LOGGING:
            self._current_state = InRestaurantOrderState.INQUEUE
        elif self._current_state == InRestaurantOrderState.INQUEUE:
            self._current_state == InRestaurantOrderState.PREPARING
        elif self._current_state == InRestaurantOrderState.PREPARING:
            self._current_state == InRestaurantOrderState.READYTOSERVE
        elif self._current_state == InRestaurantOrderState.READYTOSERVE:
            self._current_state == InRestaurantOrderState.COMPLETE
        else:
            pass


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
            "menu_items": self._menu_items,
        }

        return dict_details