from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById(mymycursor):
        pass

    @abstractmethod    
    def GetCustomerByUsername(mycursor):
        pass

    @abstractmethod
    def RegisterCustomer(mycursor):
        pass

    @abstractmethod
    def UpdateCustomer(mycursor):
        pass

    @abstractmethod
    def DeleteCustomer(mycursor):
        pass

class CustomerService (ICustomerService):
    def GetCustomerById(mycursor):
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


    def GetCustomerByUsername(mycursor):
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


    def RegisterCustomer(mycursor):
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

    def UpdateCustomer(mycursor):
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
            return False
        else:
            print("Customer updated successfully.")
            return True

    def DeleteCustomer(mycursor):
        customerId = int(input("Enter customer Id: "))
        try:
            mycursor.execute(f"DELETE FROM Customer WHERE customerId = {customerId};")
        except:
            print("Failed to delete data from the database.")
        else:
            print("Data deleted successfully.")

