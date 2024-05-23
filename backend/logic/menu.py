class Menu:

    def __init__(self, db_access):
        self.db_access = db_access
        self._menu_items = []

    def loadMenuItems(self, MenuItem):
        unorganized_menu = self.db_access.make_query("SELECT MenuItemID, Name, Description, Price FROM MenuItem WHERE MenuStatus = TRUE")
        self._menu_items = []
        for item in unorganized_menu:
            new_item = MenuItem(item[0], item[1], item[2], item[3])
            self._menu_items.append(new_item)
        return self._menu_items

    def createNewMenuItem(self, Name, Description, Price):
        next_id = self.db_access.make_query("SELECT MAX(MenuItemID) FROM MenuItem")[0][0] + 1
        
        self.db_access.make_query("INSERT INTO MenuItem (MenuItemID, Name, Description, Price, MenuStatus) VALUES (%s, %s, %s, %s, TRUE)", 
                                  (next_id, Name, Description, Price))
        
        for day_id in range(7):
            self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES (%s, %s, 0)", (next_id, day_id))
