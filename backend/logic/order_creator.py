from order_mediator import OrderMediator
class OrderCreator:

    _order_mediator: OrderMediator

    def __init__(self, order_mediator) -> None:
        self._order_mediator = order_mediator
    
    def confirm_payment(self, order_dict: dict) -> bool:
        # Will typically check with a third party vendor for payment,
        # however that has been skipped in this case.

        return True

    def create_order(self, order_dict) -> bool:
        self._order_mediator.create_order(order_dict)
        
        return True