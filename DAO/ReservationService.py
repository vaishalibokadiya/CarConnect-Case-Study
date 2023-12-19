import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')
from Util import DBConnUtil,DBPropertyUtil

from abc import ABC, abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def GetReservationById():
        pass

    @abstractmethod
    def GetReservationsByCustomerId():
        pass

    @abstractmethod
    def CreateReservation():
        pass

    @abstractmethod
    def UpdateReservation():
        pass

    @abstractmethod
    def CancelReservation():
        pass

class ReservationService (IReservationService):
    def GetReservationById():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
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

    def GetReservationsByCustomerId():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
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

    def CreateReservation():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerID=int(input("Enter customer id: "))
            vehicleID=int(input("Enter vehicle id: "))
            startDate=input("Enter start date: ")
            endDate=input("Enter end date: ")
            totalCost=float(input("Enter total cost: "))
            status=input("Enter status: ")
            try:
                mycursor.execute(f"INSERT INTO Reservation (customerId, vehicleId, startDate, endDate, totalCost, status) VALUES ({customerID},{vehicleID},'{startDate}','{endDate}',{totalCost},'{status}');")
            except Exception as e:
                print(e)
            else:
                print("Reservation created successfully.")

    def UpdateReservation():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
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


    def CancelReservation():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            reservationId = int(input("Enter ID of the reservation you want to cancel: "))
            try:
                mycursor.execute(f"DELETE FROM Reservation WHERE reservationId={reservationId};")
            except:
                print("Failed to cancel reservation from the database.")
            else:
                print("Reservation cancelled successfully.")