import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from EXCEPTION import ReservationException

from abc import ABC, abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(mycursor):
        pass

    @abstractmethod
    def GetReservationsByCustomerId(mycursor):
        pass

    @abstractmethod
    def CreateReservation(mycursor):
        pass

    @abstractmethod
    def UpdateReservation(mycursor):
        pass

    @abstractmethod
    def CancelReservation(mycursor):
        pass

class ReservationService (IReservationService):
    def GetReservationById(mycursor):
        reservationId = int(input("Enter reservation id: "))
        try:
            mycursor.execute(f"SELECT * FROM Reservation WHERE reservationId={reservationId};")
        except:
            print("Failed to fetch reservation details from the database.")
        else:
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            print("Reservation details fetched successfully.")

    def GetReservationsByCustomerId(mycursor):
        customerId = int(input("Enter customer ID:: "))
        try:
            mycursor.execute(f"SELECT * FROM Reservation WHERE customerId={customerId};")
        except:
            print("Failed to fetch reservation details from the database.")
        else:
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            print("Reservation details fetched successfully.")

    def CreateReservation(mycursor):
        customerID=int(input("Enter customer id: "))
        vehicleID=int(input("Enter vehicle id: "))
        startDate=input("Enter start date: ")
        endDate=input("Enter end date: ")
        totalCost=float(input("Enter total cost: "))
        status=input("Enter status: ")
        try:
            mycursor.execute(f"INSERT INTO Reservation (customerId, vehicleId, startDate, endDate, totalCost, status) VALUES ({customerID},{vehicleID},'{startDate}','{endDate}',{totalCost},'{status}');")
        except ReservationException as e:
            print(e.message)
        else:
            print("Reservation created successfully.")

    def UpdateReservation(mycursor):
        reservationId=int(input("Enter reservation id: "))
        customerID=int(input("Enter customer id: "))
        vehicleID=int(input("Enter vehicle id: "))
        startDate=input("Enter start date: ")
        endDate=input("Enter end date: ")
        totalCost=int(input("Enter total cost: "))
        status=input("Enter status: ")
        try:
            mycursor.execute(f"UPDATE Reservation SET customerId={customerID}, vehicleId={vehicleID}, startDate='{startDate}', endDate='{endDate}', totalCost={totalCost}, status='{status}' WHERE reservationId={reservationId});")
        except:
            print("Failed to update reservation in the database.")
        else:
            print("Reservation updated successfully.")


    def CancelReservation(mycursor):
        reservationId = int(input("Enter ID of the reservation you want to cancel: "))
        try:
            mycursor.execute(f"DELETE FROM Reservation WHERE reservationId={reservationId};")
        except:
            print("Failed to cancel reservation from the database.")
        else:
            print("Reservation cancelled successfully.")