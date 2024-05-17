from .order import Order
from .order_enumerators import TakeawayOrderState

class TakeawayOrder(Order):

    _current_state: TakeawayOrderState
    _customer: str

    def __init__(self, order_number: int):
        super().__init__(order_number)

    def advanceState(self):
        self._current_state = TakeawayOrderState(self._current_state + 1)

    def getState(self):
        return self._current_state

    def setCustomer(self, customer: str):
        self._customer = customer

    def setLocation(self, location: str):
        print("Hello there, I don't know why I have been called")

    def getDetails(self):
        dictDetails = {
            "type": "takeaway",
            "order_number": self._order_number,
            "location": "takeaway",
            "customer": self._customer,
            "menu_items": self._menu_items
        }