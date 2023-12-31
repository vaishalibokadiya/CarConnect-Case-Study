import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from AuthenticationException import AuthenticationException
class Admin:
    def __init__(self, adminId, firstName, lastName, email, phoneNumber, userName, password, role, joinDate):
        self.adminId = adminId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.userName = userName
        self.password = password
        self.role = role
        self.joinDate = joinDate

    def Authenticate(self, password):
        if password==self.password:
            return True
        else:
            raise AuthenticationException
