import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')
from Util import DBConnUtil,DBPropertyUtil

from abc import ABC, abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById():
        pass

    @abstractmethod
    def GetAvailableVehicles():
        pass

    @abstractmethod
    def AddVehicle():
        pass

    @abstractmethod
    def UpdateVehicle():
        pass

    @abstractmethod
    def RemoveVehicle():
        pass

class VehicleService (IVehicleService):
    def GetVehicleById():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            vehicleId = int(input("Enter vehicle Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Vehicle WHERE vehicleId = {vehicleId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                vehicles = mycursor.fetchall()
                for v in vehicles:
                    print(v)
                print("Data fetched successfully.")

    def GetAvailableVehicles():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            try:
                mycursor.execute(f"SELECT * FROM Vehicle WHERE availability = true;")
            except:
                print("Failed to fetch data from the database.")
            else:
                vehicles=mycursor.fetchall()
                for v in vehicles:
                    print(v)
                print("Data fetched successfully.")

    def AddVehicle():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            model=input("Enter model name: ")
            make=input("Enter make: ")
            year=input("Enter year: ")
            color=input("Enter color: ")
            registrationNumber=input("Enter registration number: ")
            availability=input("Enter availability: ")
            dailyRate=input("Enter daily rate: ")
            try:
                mycursor.execute(f"INSERT INTO Vehicle (model, make, year, color, registrationNumber, availability, dailyRate) VALUES ('{model}','{make}','{year}','{color}','{registrationNumber}','{availability}','{dailyRate}');")
            except:
                print("Failed to insert data from the database.")
            else:
                print("Data inserted successfully.")

    def UpdateVehicle():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            vehicleId = int(input("Enter ID of the vehicle you want to update: "))
            model=input("Enter model name: ")
            make=input("Enter make: ")
            year=input("Enter year: ")
            color=input("Enter color: ")
            registrationNumber=input("Enter registration number: ")
            availability=input("Enter availability: ")
            dailyRate=input("Enter daily rate: ")
            try:
                mycursor.execute(f"UPDATE Vehicle SET model='{model}', make='{make}', year='{year}', color='{color}', registrationNumber='{registrationNumber}', availability='{availability}', dailyRate='{dailyRate}' WHERE vehicleId={vehicleId};")
            except:
                print("Failed to update vehicle from the database.")
            else:
                print("Vehicle updated successfully.")

    def RemoveVehicle():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            vehicleId = int(input("Enter ID of the vehicle you want to remove: "))
            try:
                mycursor.execute(f"DELETE FROM Vehicle WHERE vehicleId={vehicleId};")
            except:
                print("Failed to remove vehicle from the database.")
            else:
                print("Vehicle removed successfully.")