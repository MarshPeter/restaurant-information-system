from .order_mediator import OrderMediator

class OrderCreator:
    _order_mediator: OrderMediator

    def set_mediator(self, order_mediator):
        self._order_mediator = order_mediator
    
    def confirm_payment(self, order_dict: dict) -> bool:
        # Typically checks with a third party vendor for payment,
        # this is skipped in this case.
        return True

    def create_order(self, order_dict) -> bool:
        self._order_mediator.create_order(order_dict)
        return True
