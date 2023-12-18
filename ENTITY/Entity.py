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

class Vehicle:
    def __init__(self, vehicleId, model, make, year, color, registrationNumber, availability, dailyRate):
        self.vehicle = vehicleId
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.registrationNumber = registrationNumber
        self.availability = availability
        self.dailyRate = dailyRate

class Reservation:
    def __init__(self, reservationId, customerId, vehicleId, startDate, endDate, totalCost, status):
        self.reservationId = reservationId
        self.customerId = customerId
        self.vehicleId = vehicleId
        self.startDate = startDate
        self.endDate = endDate
        self.totalCost = totalCost
        self.status = status

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
            return False

