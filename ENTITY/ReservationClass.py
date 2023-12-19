class Reservation:
    def __init__(self, reservationId, customerId, vehicleId, startDate, endDate, totalCost, status):
        self.reservationId = reservationId
        self.customerId = customerId
        self.vehicleId = vehicleId
        self.startDate = startDate
        self.endDate = endDate
        self.totalCost = totalCost
        self.status = status