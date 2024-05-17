from abc import ABC, abstractmethod

class Order(ABC):

    _customer: str
    _menu_items: list[str]
    _order_number: int

    def __init__(self, order_number: int):
        self._order_number = order_number
        self._menuItems = []

    def addMenuItem(self, menu_item: str) -> None:
        self._menu_items.append(menu_item)

    def getMenuItems(self) -> list[str]:
        return self._menu_items.copy()

    @abstractmethod
    def advanceState(self):
        pass

    def getState(self):
        pass
    
    @abstractmethod
    def setCustomer(self, customer: str):
        pass

    def setLocation(self, location: str):
        pass

    def getDetails(self) -> dict[str, str]:
        pass
