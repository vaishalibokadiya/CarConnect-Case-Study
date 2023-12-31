import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from AdminException import AdminNotFoundException

from abc import ABC, abstractmethod

class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(mycursor,mydb):
        pass

    @abstractmethod
    def GetAdminByUsername(mycursor,mydb):
        pass

    @abstractmethod
    def RegisterAdmin(mycursor,mydb):
        pass

    @abstractmethod
    def UpdateAdmin(mycursor,mydb):
        pass

    @abstractmethod
    def DeleteAdmin(mycursor,mydb):
        pass

class AdminService (IAdminService):
    def GetAdminById(mycursor,mydb):
        adminId = int(input("Enter admin ID: "))
        try:
            mycursor.execute(f"SELECT * FROM Admin WHERE adminId={adminId};")
        except AdminNotFoundException as e:
            print(e.message)
        else:
            rows = mycursor.fetchall()
            for row in rows:
                print(row)
            print("Admin details fetched successfully.")

    def GetAdminByUsername(mycursor,mydb):
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

    def RegisterAdmin(mycursor,mydb):
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
            mydb.commit()
        except:
            print("Failed to register admin in the database.")
        else:
            print("Admin registered successfully.")

    def UpdateAdmin(mycursor,mydb):
        adminId=int(input("Enter admin id: "))
        firstName=input("Enter first name: ")
        lastName=input("Enter last name: ")
        email=input("Enter email: ")
        phoneNumber=input("Enter phone number: ")
        username=input("Enter username: ")
        password=input("Enter password: ")
        role=input("Enter role: ")
        joinDate=input("Enter join date: ")
        try:
            mycursor.execute(f"UPDATE Admin SET firstName='{firstName}', lastName='{lastName}', email='{email}', phoneNumber='{phoneNumber}', username='{username}', password='{password}', role='{role}', joinDate='{joinDate}' WHERE adminId={adminId};")
            mydb.commit()
        except:
            print("Failed to update admin in the database.")
        else:
            print("Admin updated successfully.")

    def DeleteAdmin(mycursor,mydb):
        adminId = int(input("Enter adminId: "))
        try:
            mycursor.execute(f"DELETE FROM Admin WHERE adminId={adminId};")
            mydb.commit()
        except:
            print("Failed to delete admin from the database.")
        else:
            print("Admin deleted successfully.")