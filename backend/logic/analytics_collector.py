from .orders.order import Order
from .order_mediator import OrderMediator
from db.db_access import DBAccess
import datetime

class AnalyticsCollector:

    def __init__(self) -> None:
        self._orderMediator = None

    def set_mediator(self, order_mediator: OrderMediator) -> None:
        self._orderMediator = order_mediator 

    # returns 1...7 as that is aligned with database
    def get_day(self) -> int:
        return datetime.datetime.today().weekday() + 1

    def analyse(self, order: Order) -> None:
        order.advance_state()
        menu_items = order.get_details()["menu_items"]

        order_id = self.log_order()
        self.connect_order_to_items(menu_items=menu_items, order_id=order_id)
        self.increment_daily_quantities(menu_items=menu_items)
        
        self._orderMediator.notify(order=order, next_step="send_alerts")

    def log_order(self) -> int:
        ord_date = datetime.date.today()  # Using today's date for example
        ord_time = datetime.datetime.now().strftime("%H:%M")  # Current time in HH:MM format
        db_access = DBAccess()
        db_access.connect()
        conn = db_access.retrieve_connection()
        cursor = conn.cursor()
        last_order_id = -1

        try:
            query = """
            INSERT INTO OrderLogs (OrdDate, OrdTime)
            VALUES (%s, %s)
            """
            values = (ord_date, ord_time)
            cursor.execute(query, values)
            conn.commit()
            last_order_id = cursor.lastrowid
            db_access.disconnect()
        except Exception as e:
            print("ERROR HAS OCCURRED: ", e)

        return last_order_id

    def connect_order_to_items(self, menu_items, order_id) -> None:
        db_access = DBAccess()
        db_access.connect()
        conn = db_access.retrieve_connection()
        cursor = conn.cursor()
        try:
            for item in menu_items:
                query = """
                INSERT INTO OrderMenuItem (OrderId, MenuItemID, Quantity)
                VALUES (%s, %s, %s)
                """
                values = (order_id, item['id'], item['quantity'])
                cursor.execute(query, values)
                conn.commit()
            db_access.disconnect()
        except Exception as e:
            print("ERROR HAS OCCURRED: ", e)
 
    def increment_daily_quantities(self, menu_items) -> None:
        day = self.get_day()
        db_access = DBAccess()
        db_access.connect()
        conn = db_access.retrieve_connection()
        cursor = conn.cursor()
        try:
            for item in menu_items:
                query = """
                INSERT INTO daysales (MenuItemId, DayID, Amount)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    Amount = Amount + %s
                """
                values = (item['id'], day, item['quantity'], item['quantity'])
                cursor.execute(query, values)
                conn.commit()
            db_access.disconnect()
        except Exception as e:
            print("ERROR HAS OCCURRED: ", e)




