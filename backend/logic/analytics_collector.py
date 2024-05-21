import datetime

class AnalyticsCollector:

    _date: datetime
    _time: datetime
    
    def __init__(self, db_access):
        self._date = datetime.datetime.today().strftime('%Y-%m-%d')
        # self.time = now.time()
        self.db_access = db_access
    
    def get_day() -> int:
        return datetime.datetime.today().weekday()
        
    def notify(self, order, db_access):
        self.item_quantity_price = []
        self.totalprice = 0
        for item in order._menu_items: #this iterates through the list o menu items and counts how many of each there are and adds them to a list
            self.added= False
            for quantity in item_quantity_price:
                if item.itemID == quantity[0]:
                    quantity[1] += 1
                    self.added=True
            if not self.added:
                self.item_quantity.append([item.itemID],[1],[0])
        for item in self.item_quantity_price: #gets the current price of each item and total price
            item[2] = self.db_access.make_query("Price from MenuItem where MenuItemID == "+item[0])
            self.itemsprice = item[2] * item[1]
            self.totalprice = self.totalprice + self.itemsprice
        
        #geting the id of the next order to place in the database so I can link it to menu items
        self.orderid = self.db_access.make_query("SELECT MAX(OrderID) FROM OrderLogs;")
        self.orderid += 1
        self.db_access.make_query("SELECT MAX(OrderID) FROM OrderLogs;")
        self.db_access.make_query("INSERT INTO OrderLogs (OrdDate, OrdTime, PricePayed) VALUES ("+ self._date +","+ self._time +","+ self.totalprice +")")
        
        for item in self.item_quantity_price:
            self.db_access.make_query("INSERT INTO OrderMenuItem (OrderID, MenuItemID, Quantity, ItemPrice) VALUES ("+ orderid +","+ item[0] +","+ item[1] +","+ item[2] +")")
            self.oldamount = self.db_access.make_query("SELECT Amount FROM DaySales WHERE MenuItemID = "+item[0]+" and DayID = "+self.get_day())
            self.newamount = self.oldamount+item[2]
            self.db_access.make_query("UPDATE DaySales Amount "+self.newamount+" WHERE MenuItemID = "+item[0]+" and DayID = "+self.get_day())
        
        