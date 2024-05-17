from .order import Order
from .order_enumerators import DeliveryOrderState

class InRestaurantOrder(Order):

    _current_state: DeliveryOrderState
    _table: str
    _customer: str

    def __init__(self, order_number: int):
        super().__init__(order_number=order_number)
        self._current_state = DeliveryOrderState.LOGGING

    def advanceState(self):
        _current_state = DeliveryOrderState(_current_state + 1)

    def getState(self):
        return self._current_state

    def setCustomer(self, customer: str):
        self._customer = customer
    
    def setLocation(self, location: str):
        self._table = "Table: " + location

    def getDetails(self) -> dict:
        dictDetails = {
            "order_number": self._order_number,
            "table": self._table,
            "customer": self._customer,
            "menu_items": self._menu_items
        }

        return dictDetails