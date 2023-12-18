class AuthenticationException:
    def __init__(self, message="Authentication failed"):
        self.message = message

class ReservationException:
    def __init__(self, message="Reservation failed"):
        self.message = message

class VehicleNotFoundException:
    def __init__(self, message="Vehicle not found"):
        self.message = message

class AdminNotFoundException:
    def __init__(self, message="Admin not found"):
        self.message = message

class InvalidInputException:
    def __init__(self, message="Input is invalid"):
        self.message = message

class DatabaseConnectionException:
    def __init__(self, message="Database connection failed"):
        self.message = message