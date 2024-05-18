from abc import ABC, abstractmethod

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order):
        pass
