from logic.builders.delivery_order_builder import DeliveryOrderBuilder
from logic.builders.in_restaurant_order_builder import InRestaurantOrderBuilder
from logic.builders.takeaway_order_builder import TakeawayOrderBuilder
from logic.order_director import OrderDirector
from logic.orders.order import Order
from .order_mediator import OrderMediator

class OrderParser:
    _order_mediator: OrderMediator
    def __init__(self):
        self._delivery_order_builder = DeliveryOrderBuilder()
        self._takeaway_order_builder = TakeawayOrderBuilder()
        self._in_restaurant_order_builder = InRestaurantOrderBuilder()
        self._order_director = OrderDirector()
    
    def set_mediator(self, order_mediator: OrderMediator) -> None:
        self._order_mediator = order_mediator

    def create_order(self, order_dict: dict) -> None:
        if order_dict["orderType"] == "inRestaurant":
            self._order_director.use_builder(self._in_restaurant_order_builder)
            order = self._order_director.build_in_restaurant_order(order_dict=order_dict)
            self._order_mediator.notify(order=order, next_step="analyse")
        if order_dict["orderType"] == "takeaway":
            self._order_director.use_builder(self._takeaway_order_builder)
            return self._order_director.build_takeaway_order(order_dict=order_dict)
        if order_dict["orderType"] == "delivery":
            self._order_director.use_builder(self._delivery_order_builder)
            return self._order_director.build_delivery_order(order_dict=order_dict)
