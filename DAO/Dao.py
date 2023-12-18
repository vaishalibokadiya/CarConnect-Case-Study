import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')
from Util import DBConnUtil,DBPropertyUtil

from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById():
        pass

    @abstractmethod    
    def GetCustomerByUsername():
        pass

    @abstractmethod
    def RegisterCustomer():
        pass

    @abstractmethod
    def UpdateCustomer():
        pass

    @abstractmethod
    def DeleteCustomer():
        pass



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


class IAdminService(ABC):
    @abstractmethod
    def GetAdminById():
        pass

    @abstractmethod
    def GetAdminByUsername():
        pass

    @abstractmethod
    def RegisterAdmin():
        pass

    @abstractmethod
    def UpdateAdmin():
        pass

    @abstractmethod
    def DeleteAdmin():
        pass

class CustomerService (ICustomerService):
    def GetCustomerById():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Customer WHERE customerId = {customerId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")


    def GetCustomerByUsername():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            userName = input("Enter customer's username: ")
            try:
                mycursor.execute(f"SELECT * FROM Customer WHERE username = '{userName}';")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")


    def RegisterCustomer():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            phoneNumber = input("Enter phone number: ")
            address = input("Enter address: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            registrationDate= input("Enter registration date: ")

            try:
                mycursor.execute(f"INSERT INTO Customer (firstName, lastName, email, phoneNumber, address, username, password, registrationDate) VALUES ('{firstName}','{lastName}','{email}','{phoneNumber}','{address}','{username}','{password}','{registrationDate}');")
            except:
                print("Failed to insert data from the database.")
            else:
                print("Data inserted successfully.")

    def UpdateCustomer():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter ID of the customer you want to update: "))
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            phoneNumber = input("Enter phone number: ")
            address = input("Enter address: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            registrationDate= input("Enter registration date: ")
            try: 
                mycursor.execute(f"UPDATE Customer SET firstName='{firstName}',lastName='{lastName}',email='{email}',phoneNumber='{phoneNumber}',address='{address}',username='{username}',password='{password}',registrationDate='{registrationDate}' WHERE customerId={customerId};")
            except:
                print("Failed to update customer from the database.")
            else:
                print("Customer updated successfully.")

    def DeleteCustomer():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"DELETE FROM Customer WHERE customerId = {customerId};")
            except:
                print("Failed to delete data from the database.")
            else:
                print("Data deleted successfully.")



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

class AdminService (IAdminService):
    def GetAdminById():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            adminId = int(input("Enter admin ID: "))
            try:
                mycursor.execute(f"SELECT * FROM Admin WHERE adminId={adminId};")
            except:
                print("Failed to fetch admin details from the database.")
            else:
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Admin details fetched successfully.")

    def GetAdminByUsername():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            username = input("Enter admin username: ")
            try:
                mycursor.execute(f"SELECT * FROM Admin WHERE username='{username}';")
            except:
                print("Failed to fetch admin details from the database.")
            else:
                rows = mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Admin details fetched successfully.")

    def RegisterAdmin():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            firstName=input("Enter first name: ")
            lastName=input("Enter last name: ")
            email=input("Enter email: ")
            phoneNumber=input("Enter phone number: ")
            username=input("Enter username: ")
            password=input("Enter password: ")
            role=input("Enter role: ")
            joinDate=input("Enter join date: ")
            try:
                mycursor.execute(f"INSERT INTO Admin (firstName, lastName, email, phoneNumber, username, password, role, joinDate) VALUES ('{firstName}','{lastName}','{email}','{phoneNumber}','{username}','{password}','{role}','{joinDate}');")
            except:
                print("Failed to register admin in the database.")
            else:
                print("Admin registered successfully.")

    def UpdateAdmin():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            adminId=int(input("Enter admin id"))
            firstName=input("Enter first name")
            lastName=input("Enter last name")
            email=input("Enter email")
            phoneNumber=input("Enter phone number")
            username=input("Enter username")
            password=input("Enter password")
            role=input("Enter role")
            joinDate=input("Enter join date")
            try:
                mycursor.execute(f"UPDATE Admin SET firstName='{firstName}', lastName='{lastName}', email='{email}', phoneNumber='{phoneNumber}', username='{username}', password='{password}', role='{role}', joinDate='{joinDate}' WHERE adminId={adminId};")
            except:
                print("Failed to update admin in the database.")
            else:
                print("Admin updated successfully.")

    def DeleteAdmin():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            adminId = int(input("Enter adminId: "))
            try:
                mycursor.execute(f"DELETE FROM Admin WHERE adminId={adminId};")
            except:
                print("Failed to delete admin from the database.")
            else:
                print("Admin deleted successfully.")

class DatabaseContext:
    @staticmethod
    def get_connection_string():
        host=input("Enter host name: ")
        user=input("Enter user name: ")
        password=input("Enter password: ")
        database=input("Enter database name: ")
        try:
            mydb = sql.connect(host=host,user=user,password=password,database=database)
        except:
            print("Unable to connect to the database.")
        else:
            print('Successfully connected to the database.')
            return mydb
        
    @staticmethod
    def get_connection_object(mydb):
        try:
            mycursor = mydb.cursor()
            
        except:
            print("Error in getting cursor object")
        else:
            print("Cursor created successfully")
            return mycursor, mydb