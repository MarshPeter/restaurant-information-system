from .order import Order
from .order_enumerators import DeliveryOrderState

class DeliveryOrder(Order):

    _current_state: DeliveryOrderState
    _address: str
    _customer: str

    def __init__(self, order_number: int):
        super().__init__(order_number=order_number)
        self._current_state(DeliveryOrderState.LOGGING)

    def advanceState(self):
        self._current_state = DeliveryOrderState(self._current_state + 1)

    def getState(self):
        return self._current_state

    def setCustomer(self, customer: str):
        self.customer = customer

    def setLocation(self, location: str):
        self._address = "Address: " + location

    def getDetails(self):
        dictDetails = {
            "type": "delivery",
            "order_number": self._order_number,
            "address": self._address,
            "customer": self._customer,
            "menu_items": self._menu_items
        }

        return dictDetails
