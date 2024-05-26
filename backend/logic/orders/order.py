from abc import ABC, abstractmethod

class Order(ABC):

    _customer: str
    _menu_items: list[dict]
    _order_number: int
    _state: str

    def __init__(self, order_number: int):
        self._order_number = order_number
        self._menu_items = []
        self._state = "Pending"  # Initial state

    def add_menu_item(self, menu_item: dict) -> None:
        self._menu_items.append(menu_item)

    def get_menu_items(self) -> list[str]:
        return self._menu_items.copy()

    def advance_state(self):
        state_order = ["Pending", "Preparing", "Ready", "Served"]
        current_index = state_order.index(self._state)
        if current_index < len(state_order) - 1:
            self._state = state_order[current_index + 1]

    def get_state(self):
        return self._state

    @abstractmethod
    def set_customer(self, customer: str):
        pass

    def set_location(self, location: str):
        pass

    def get_details(self):
        return {
            "order_number": self._order_number,
            "customer": self._customer,
            "menu_items": self._menu_items,
            "state": self._state
        }
