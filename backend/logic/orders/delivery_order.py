from .order import Order
from .order_enumerators import DeliveryOrderState

class DeliveryOrder(Order):

    _current_state: DeliveryOrderState
    _address: str
    _customer: str

    def __init__(self, order_number: int):
        super().__init__(order_number=order_number)
        self._current_state = DeliveryOrderState.LOGGING

    def advance_state(self):
        self._current_state = DeliveryOrderState(self._current_state + 1)

    def get_state(self):
        return self._current_state

    def set_customer(self, customer: str):
        self.customer = customer

    def set_location(self, location: str):
        self._address = "Address: " + location

    def get_details(self):
        dictDetails = {
            "type": "delivery",
            "order_number": self._order_number,
            "address": self._address,
            "customer": self._customer,
            "menu_items": self._menu_items
        }

        return dictDetails
