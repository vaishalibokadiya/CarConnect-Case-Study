# Exception for vehicle not found
class VehicleNotFoundException:
    def __init__(self, message="Vehicle not found"):
        self.message = message