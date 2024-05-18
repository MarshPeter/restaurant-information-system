from .builders.delivery_order_builder import DeliveryOrderBuilder
from .builders.in_restaurant_order_builder import InRestaurantOrderBuilder
from .builders.takeaway_order_builder import TakeawayOrderBuilder
from .order_director import OrderDirector
from .orders.order import Order

class OrderParser:

    def __init__(self):
        self._delivery_order_builder = DeliveryOrderBuilder()
        self._takeaway_order_builder = TakeawayOrderBuilder()
        self._in_restaurant_order_builder = InRestaurantOrderBuilder()
        self._order_director = OrderDirector()

    def createOrder(self, order_dict: dict) -> Order:
        if order_dict["orderType"] == "inRestaurant":
            self._order_director.use_builder(self._in_restaurant_order_builder)
            return self._order_director.build_in_restaurant_order()
        if order_dict["orderType"] == "takeaway":
            self._order_director.use_builder(self._takeaway_order_builder)
            return self._order_director.build_takeaway_order()
        if order_dict["orderType"] == "delivery":
            self._order_director.use_builder(self._delivery_order_builder)
            return self._order_director.build_delivery_order()


