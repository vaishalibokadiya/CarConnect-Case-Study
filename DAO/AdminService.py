import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')
from Util import DBConnUtil,DBPropertyUtil

from abc import ABC, abstractmethod

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