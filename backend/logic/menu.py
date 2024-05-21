class Menu:

    _menu_items: list[dict]
    
    def __init__(self, db_access):
        self.db_access = db_access
    def loadMenuItems(self)
        unorganisedmenu = self.db_access.make_query("SELECT MenuItemID, Name, Description, Price FROM MenuItem WHERE MenuStatus == TRUE")
        for item in unorganisedmenu
            newitem = MenuItem(unorganisedmenu.MenuItemID, unorganisedmenu.Name, unorganisedmenu.Description, unorganisedmenu.Price)
            _menu_items.append(newitem)
        return _menu_items
    def createNewMenuitem(Name, Description, Price)
        nextID = self.db_access.make_query("SELECT MAX(MenuItemID) FROM MenuItem")
        nextID++
        self.db_access.make_query("SELECT MAX(MenuItemID) FROM MenuItem")
        self.db_access.make_query("INSERT INTO MenuItem (Name, Description, Price) VALUES ("+ Name +","+ Description +","+ Price +")")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",0,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",1,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",2,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",3,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",4,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",5,0)")
        self.db_access.make_query("INSERT INTO DaySales (MenuItemID, DayID, Amount) VALUES ("+ nextID +",6,0)")
    