from .orders.order import Order

class OrderMediator:
    def __init__(self, order_parser, order_creator, order_notifier, analytics_collector):
        self._order_parser = order_parser
        self._order_creator = order_creator
        self._order_notifier = order_notifier
        self._analytics_collector = analytics_collector

    def notify(self, order: Order, next_step: str):
        if next_step == "analyse":
            print(order.get_details())
            print(order.get_state().name)
            # send to analyticsCollector
            # in analytics collector order state should advance after analytics has been collected
            order.advance_state()
            print(order.get_state().name)
            self.notify(order=order, next_step="ready_to_cook")

        elif next_step == "ready_to_cook":
            self._order_notifier.send_notifications(notify_type="ready_to_cook", order=order)
            order.advance_state()
            self.notify(order=order, next_step="ready_to_serve")

        elif next_step == "ready_to_serve":
            self._order_notifier.send_notifications(notify_type="ready_to_serve", order=order)

    def create_order(self, order_dict):
        self._order_parser.create_order(order_dict)
