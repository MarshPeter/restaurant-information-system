import datetime

class AnalyticsCollector:

    def __init__(self, db_access):
        self._date = datetime.datetime.today().strftime('%Y-%m-%d')
        self._time = datetime.datetime.today().strftime('%H:%M:%S')
        self.db_access = db_access

    @staticmethod
    def get_day() -> int:
        return datetime.datetime.today().weekday()

    def notify(self, order):
        self.item_quantity_price = []
        self.total_price = 0

        for item in order._menu_items:
            added = False
            for quantity in self.item_quantity_price:
                if item.itemID == quantity[0]:
                    quantity[1] += 1
                    added = True
            if not added:
                self.item_quantity_price.append([item.itemID, 1, 0])
        
        for item in self.item_quantity_price:
            item[2] = self.db_access.make_query("SELECT Price FROM MenuItem WHERE MenuItemID = %s", (item[0],))[0][0]
            items_price = item[2] * item[1]
            self.total_price += items_price

        order_id = self.db_access.make_query("SELECT MAX(OrderID) FROM OrderLogs;")[0][0] + 1

        self.db_access.make_query(
            "INSERT INTO OrderLogs (OrdDate, OrdTime, PricePayed) VALUES (%s, %s, %s)",
            (self._date, self._time, self.total_price)
        )

        for item in self.item_quantity_price:
            self.db_access.make_query(
                "INSERT INTO OrderMenuItem (OrderID, MenuItemID, Quantity, ItemPrice) VALUES (%s, %s, %s, %s)",
                (order_id, item[0], item[1], item[2])
            )

            old_amount = self.db_access.make_query(
                "SELECT Amount FROM DaySales WHERE MenuItemID = %s AND DayID = %s",
                (item[0], self.get_day())
            )[0][0]

            new_amount = old_amount + item[1]

            self.db_access.make_query(
                "UPDATE DaySales SET Amount = %s WHERE MenuItemID = %s AND DayID = %s",
                (new_amount, item[0], self.get_day())
            )
