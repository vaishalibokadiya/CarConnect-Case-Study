# Exception for error while creating a reservation
class ReservationFailedException:
    def __init__(self, message="Reservation failed"):
        self.message = message
