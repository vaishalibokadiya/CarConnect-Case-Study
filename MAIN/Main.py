import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/DAO')
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')

from CustomerService import CustomerService
from ReservationService import ReservationService
from VehicleService import VehicleService
from AdminService import AdminService

from Util import DBConnUtil,DBPropertyUtil

try:
    [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
except:
    print("Error in connection")

def show_menu():
    print("1: Customer Services")
    print("2: Reservation Services")
    print("3: Vehicle Services")
    print("4: Admin Services")
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("1: Get customer by id")
        print("2: Get customer by username")
        print("3: Register customer")
        print("4: Update customer information")
        print("5: Delete customer")

        choice2=int(input("Enter your choice: "))
        if choice2==1:
            CustomerService.GetCustomerById(mycursor)
        elif choice2==2:
            CustomerService.GetAdminByUsername(mycursor)
        elif choice2==3:
            CustomerService.RegisterCustomer(mycursor)
        elif choice2==4:
            CustomerService.UpdateCustomer(mycursor)
        elif choice2==5:
            CustomerService.DeleteCustomer(mycursor)
        else:
            return 

    elif choice==2:
        print("1: Get vehicle by id")
        print("2: Get available vehicles")
        print("3: Add vehicle")
        print("4: Update vehicle")
        print("5: Remove vehicle")

        choice2=int(input("Enter your choice: "))
        if choice2==1:
            VehicleService.GetVehicleById(mycursor)
        elif choice2==2:
            VehicleService.GetAvailableVehicles(mycursor)
        elif choice2==3:
            VehicleService.AddVehicle(mycursor)
        elif choice2==4:
            VehicleService.UpdateVehicle(mycursor)
        elif choice2==5:
            VehicleService.RemoveVehicle(mycursor)
        else:
            return 

    elif choice==3:
        print("1: Get reservation by id")
        print("2: Get reservation by customer id")
        print("3: Create reservation")
        print("4: Update reservation")
        print("5: Cancel reservation")

        choice2=int(input("Enter your choice: "))
        if choice2==1:
            ReservationService.GetReservationById(mycursor)
        elif choice2==2:
            ReservationService.GetReservationsByCustomerId(mycursor)
        elif choice2==3:
            ReservationService.CreateReservation(mycursor)
        elif choice2==4:
            ReservationService.UpdateReservation(mycursor)
        elif choice2==5:
            ReservationService.CancelReservation(mycursor)
        else:
            return 
        

    elif choice==4:
        print("1: Get admin by id")
        print("2: Get admin by username")
        print("3: Register admin")
        print("4: Update admin information")
        print("5: Delete admin")

        choice2=int(input("Enter your choice: "))
        if choice2==1:
            AdminService.GetAdminById(mycursor)
        elif choice2==2:
            AdminService.GetAdminByUsername(mycursor)
        elif choice2==3:
            AdminService.RegisterAdmin(mycursor)
        elif choice2==4:
            AdminService.UpdateAdminInfo(mycursor)
        elif choice2==5:
            AdminService.DeleteAdmin(mycursor)
        else:
            return 

show_menu()


