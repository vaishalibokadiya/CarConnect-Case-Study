import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from ReservationException import ReservationFailedException

from abc import ABC, abstractmethod
from datetime import datetime
# Abstract class for reservation
class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(mycursor,mydb):
        pass

    @abstractmethod
    def GetReservationsByCustomerId(mycursor,mydb):
        pass

    @abstractmethod
    def CreateReservation(mycursor,mydb):
        pass

    @abstractmethod
    def UpdateReservation(mycursor,mydb):
        pass

    @abstractmethod
    def CancelReservation(mycursor,mydb):
        pass

def convert_mysql_decimal_to_float(decimal_object):
    if (decimal_object == None):
        return None
    else:
        return float(decimal_object)


# Implementation of IReservationService
class ReservationService (IReservationService):
    # Get reservation details using reservation id
    def GetReservationById(mycursor,mydb):
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

    # Get reservation details using customer Id
    def GetReservationsByCustomerId(mycursor,mydb):
        customerId = int(input("Enter customer ID: "))
        try:
            mycursor.execute(f"SELECT * FROM Reservation WHERE customerId={customerId};")
        except:
            print("Failed to fetch reservation details from the database.")
        else:
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            print("Reservation details fetched successfully.")

    # Create new reservation
    def CreateReservation(mycursor,mydb):
        customerID=int(input("Enter customer id: "))
        vehicleID=int(input("Enter vehicle id: "))
        startDate=input("Enter start date: ")
        endDate=input("Enter end date: ")
        status=input("Enter status: ")
        start=datetime.strptime(startDate, "%Y-%m-%d")
        end=datetime.strptime(endDate, "%Y-%m-%d")
        mycursor.execute(f"SELECT dailyRate FROM Vehicle WHERE vehicleId={vehicleID}")
        value=mycursor.fetchone()
        dailyRate=convert_mysql_decimal_to_float(value[0])
        noOfDays=(end-start).days
        totalCost=int(noOfDays)*dailyRate
        try:
            mycursor.execute(f"INSERT INTO Reservation (customerId, vehicleId, startDate, endDate, totalCost, status) VALUES ({customerID},{vehicleID},'{startDate}','{endDate}',{totalCost},'{status}');")
            mydb.commit()
        except ReservationFailedException as e:
            print(e.message)
        else:
            print("Reservation created successfully.")

    # Update an existing reservation
    def UpdateReservation(mycursor,mydb):
        reservationId=int(input("Enter reservation id: "))
        customerID=int(input("Enter customer id: "))
        vehicleID=int(input("Enter vehicle id: "))
        startDate=input("Enter start date: ")
        endDate=input("Enter end date: ")
        start=datetime.strptime(startDate, "%Y-%m-%d")
        end=datetime.strptime(endDate, "%Y-%m-%d")
        mycursor.execute(f"SELECT dailyRate FROM Vehicle WHERE vehicleId={vehicleID}")
        value=mycursor.fetchone()
        dailyRate=convert_mysql_decimal_to_float(value[0])
        noOfDays=(end-start).days
        totalCost=int(noOfDays)*dailyRate
        status=input("Enter status: ")
        try:
            mycursor.execute(f"UPDATE Reservation SET customerId={customerID}, vehicleId={vehicleID}, startDate='{startDate}', endDate='{endDate}', totalCost={totalCost}, status='{status}' WHERE reservationId={reservationId};")
            mydb.commit()
        except:
            print("Failed to update reservation in the database.")
        else:
            print("Reservation updated successfully.")

    # Delete a reservation
    def CancelReservation(mycursor,mydb):
        reservationId = int(input("Enter ID of the reservation you want to cancel: "))
        try:
            mycursor.execute(f"DELETE FROM Reservation WHERE reservationId={reservationId};")
            mydb.commit()
        except:
            print("Failed to cancel reservation from the database.")
        else:
            print("Reservation cancelled successfully.")