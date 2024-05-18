from .builders.order_builder import OrderBuilder

class Director:

    def __init__(self):
        self._builder = None

    def use_builder(self, builder: OrderBuilder):
        self._builder = builder

    def build_in_restaurant_order(self, order_dict):
        self._builder.reset_order()
        
        if "customerName" in order_dict():
            self._builder.set_customer(order_dict["customerName"])
        else:
            self._builder.set_customer()

        self._builder.set_destination(order_dict["table"])

        for menu_item in order_dict["menuItems"]:
            self._builder.add_menu_item(menu_item)

        return self._builder.get_order()

    def build_delivery_order(self, order_dict):
        self._builder.reset_order()
        
        if "customerName" in order_dict():
            self._builder.set_customer(order_dict["customerName"])
        else:
            self._builder.set_customer()

        self._builder.set_destination(order_dict["address"])

        for menu_item in order_dict["menuItems"]:
            self._builder.add_menu_item(menu_item)

        return self._builder.get_order()

    def build_takeaway_order(self, order_dict):
        self._builder.reset_order()
        
        if "customerName" in order_dict():
            self._builder.set_customer(order_dict["customerName"])
        else:
            self._builder.set_customer()

        for menu_item in order_dict["menuItems"]:
            self._builder.add_menu_item(menu_item)

        return self._builder.get_order()
