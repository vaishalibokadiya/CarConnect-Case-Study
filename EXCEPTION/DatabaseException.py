# Exception for database connection errors
class DatabaseConnectionException:
    def __init__(self, message="Database connection failed"):
        self.message = message