class Customer:
    def __init__(self, customerId, firstName, lastName, email, phoneNumber, address, userName, password, registrationDate):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.userName = userName
        self.password = password
        self.registrationDate = registrationDate

    def Authenticate(self, password):
        if password==self.password:
            return True
        else:
            return False