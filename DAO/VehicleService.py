import sys 
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from VehicleException import VehicleNotFoundException

from abc import ABC, abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById(mycursor,mydb):
        pass

    @abstractmethod
    def GetAvailableVehicles(mycursor,mydb):
        pass

    @abstractmethod
    def AddVehicle(mycursor,mydb):
        pass

    @abstractmethod
    def UpdateVehicle(mycursor,mydb):
        pass

    @abstractmethod
    def RemoveVehicle(mycursor,mydb):
        pass

class VehicleService (IVehicleService):
    def GetVehicleById(mycursor,mydb):
        vehicleId = int(input("Enter vehicle Id: "))
        try:
            mycursor.execute(f"SELECT * FROM Vehicle WHERE vehicleId = {vehicleId};")
        except VehicleNotFoundException as e:
            print(e.message)
            return False
        else:
            vehicles = mycursor.fetchall()
            for v in vehicles:
                print(v)
            print("Data fetched successfully.")
            return True

    def GetAvailableVehicles(mycursor,mydb):
        try:
            mycursor.execute(f"SELECT * FROM Vehicle WHERE availability = true;")
        except:
            print("Failed to fetch data from the database.")
            return False
        else:
            vehicles=mycursor.fetchall()
            for v in vehicles:
                print(v)
            print("Data fetched successfully.")
            return True

    def AddVehicle(mycursor,mydb):
        model=input("Enter model name: ")
        make=input("Enter make: ")
        year=input("Enter year: ")
        color=input("Enter color: ")
        registrationNumber=input("Enter registration number: ")
        availability=input("Enter availability: ")
        dailyRate=input("Enter daily rate: ")
        try:
            mycursor.execute(f"INSERT INTO Vehicle (model, make, year, color, registrationNumber, availability, dailyRate) VALUES ('{model}','{make}','{year}','{color}','{registrationNumber}','{availability}','{dailyRate}');")
            mydb.commit()
        except:
            print("Failed to insert data from the database.")
            return False
        else:
            print("Data inserted successfully.")
            return True

    def UpdateVehicle(mycursor,mydb):
        vehicleId = int(input("Enter ID of the vehicle you want to update: "))
        model=input("Enter model name: ")
        make=input("Enter make: ")
        year=input("Enter year: ")
        color=input("Enter color: ")
        registrationNumber=input("Enter registration number: ")
        availability=input("Enter availability: ")
        dailyRate=float(input("Enter daily rate: "))
        try:
            mycursor.execute(f"UPDATE Vehicle SET model='{model}', make='{make}', year='{year}', color='{color}', registrationNumber='{registrationNumber}', availability='{availability}', dailyRate='{dailyRate}' WHERE vehicleId={vehicleId};")
            mydb.commit()
        except:
            print("Failed to update vehicle from the database.")
            return False
        else:
            print("Vehicle updated successfully.")
            return True

    def RemoveVehicle(mycursor,mydb):
        vehicleId = int(input("Enter ID of the vehicle you want to remove: "))
        try:
            mycursor.execute(f"DELETE FROM Vehicle WHERE vehicleId={vehicleId};")
            mydb.commit()
        except:
            print("Failed to remove vehicle from the database.")
        else:
            print("Vehicle removed successfully.")