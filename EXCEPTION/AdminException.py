# Exception for admin not found
class AdminNotFoundException:
    def __init__(self, message="Admin not found"):
        self.message = message