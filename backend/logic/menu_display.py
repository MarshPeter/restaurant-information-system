class MenuDisplay:

    _account_authenticator: AccountAuthenticator
    _menu: Menu
    _email_address:str#???
    
    def __init__(self):
        self._account_authenticator = AccountAuthenticator()
        self._menu = Menu()
        self._email_address = ""
        
    def login(self, username, password)
        return self._account_authenticator(username, password)
    
    def requestCurrentMenu(self)
        return self._menu.loadMenuItems()
    
    def createNewMenuItem(self, Name, Description, Price)
        self.menu.createNewMenuitem(Name, Description, Price)
    
    #displayMenu seems redundant
        