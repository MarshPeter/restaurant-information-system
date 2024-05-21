import datetime

class AccountAuthenticator:

    def __init__(self, db_access):
		  self.db_access = db_access
	 
	 def authenticate(self,username,password)
			self.correctusername = self.db_access.make_query("SELECT UserName FROM Account WHERE UserName == "username")
            if username == correctusername
                self.correctPassword = self.db_access.make_query("SELECT PassWord FROM Account WHERE UserName == "username")
                if password == self.correctpassword
                    return true
                else
                return false
            else
            return false
			
