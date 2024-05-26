from abc import ABC, abstractmethod
from .orders.order import Order 

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order: Order) -> None:
        pass
