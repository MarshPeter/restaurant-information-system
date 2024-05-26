from abc import ABC, abstractmethod

class Order(ABC):

    _customer: str
    _menu_items: list[dict]
    _order_number: int

    def __init__(self, order_number: int):
        self._order_number = order_number
        self._menu_items = []

    def add_menu_item(self, menu_item: dict) -> None:
        self._menu_items.append(menu_item)

    def get_menu_items(self) -> list[str]:
        return self._menu_items.copy()

    def advance_state(self):
        pass

    def get_state(self):
        pass

    @abstractmethod
    def set_customer(self, customer: str):
        pass

    def set_location(self, location: str):
        pass

    def get_details(self):
        pass
