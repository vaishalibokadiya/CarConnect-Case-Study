from abc import ABC, abstractmethod

import bcrypt
from datetime import date

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = str(bcrypt.hashpw(password.encode('utf-8'), salt))[2:-1]
    return hashed_password

# Abstract class for custromer service
class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById(mymycursor,mydb):
        pass

    @abstractmethod    
    def GetCustomerByUsername(mycursor,mydb):
        pass

    @abstractmethod
    def RegisterCustomer(mycursor,mydb):
        pass

    @abstractmethod
    def UpdateCustomer(mycursor,mydb):
        pass

    @abstractmethod
    def DeleteCustomer(mycursor,mydb):
        pass

# Implementation of Customer Service
class CustomerService (ICustomerService):
    # Get customer details using customer id
    def GetCustomerById(mycursor,mydb):
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

    # Get customer details using customer username
    def GetCustomerByUsername(mycursor,mydb):
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

    # Create a new customer
    def RegisterCustomer(mycursor,mydb):
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        phoneNumber = input("Enter phone number: ")
        address = input("Enter address: ")
        username = input("Enter username: ")
        password=str(hash_password(input("Enter password: ")))
        registrationDate= date.today()
        try:
            mycursor.execute(f"INSERT INTO Customer (firstName, lastName, email, phoneNumber, address, username, password, registrationDate) VALUES ('{firstName}','{lastName}','{email}','{phoneNumber}','{address}','{username}','{password}','{registrationDate}');")
            mydb.commit()
        except:
            print("Failed to insert data from the database.")
        else:
            print("Data inserted successfully.")

    # Update an existing customer using customer id
    def UpdateCustomer(mycursor,mydb):
        customerId = int(input("Enter ID of the customer you want to update: "))
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        phoneNumber = input("Enter phone number: ")
        address = input("Enter address: ")
        username = input("Enter username: ")
        password=str(hash_password(input("Enter password: ")))
        registrationDate= input("Enter registration date: ")
        try: 
            mycursor.execute(f"UPDATE Customer SET firstName='{firstName}',lastName='{lastName}',email='{email}',phoneNumber='{phoneNumber}',address='{address}',username='{username}',password='{password}',registrationDate='{registrationDate}' WHERE customerId={customerId};")
            mydb.commit()
        except:
            print("Failed to update customer from the database.")
            return False
        else:
            print("Customer updated successfully.")
            return True

    # Delete a customer
    def DeleteCustomer(mycursor,mydb):
        customerId = int(input("Enter customer Id: "))
        try:
            mycursor.execute(f"DELETE FROM Customer WHERE customerId = {customerId};")
            mydb.commit()
        except:
            print("Failed to delete data from the database.")
        else:
            print("Data deleted successfully.")

