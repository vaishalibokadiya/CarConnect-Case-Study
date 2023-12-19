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

