import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/DAO')
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')

from CustomerService import CustomerService
from ReservationService import ReservationService
from VehicleService import VehicleService
from AdminService import AdminService

from Util import DBConnUtil,DBPropertyUtil

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
            CustomerService.GetCustomerById()
        elif choice2==2:
            CustomerService.GetAdminByUsername()
        elif choice2==3:
            CustomerService.RegisterCustomer()
        elif choice2==4:
            CustomerService.UpdateCustomer()
        elif choice2==5:
            CustomerService.DeleteCustomer()
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
            VehicleService.GetVehicleById()
        elif choice2==2:
            VehicleService.GetAvailableVehicles()
        elif choice2==3:
            VehicleService.AddVehicle()
        elif choice2==4:
            VehicleService.UpdateVehicle()
        elif choice2==5:
            VehicleService.RemoveVehicle()
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
            ReservationService.GetReservationById()
        elif choice2==2:
            ReservationService.GetReservationsByCustomerId()
        elif choice2==3:
            ReservationService.CreateReservation()
        elif choice2==4:
            ReservationService.UpdateReservation()
        elif choice2==5:
            ReservationService.CancelReservation()
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
            AdminService.GetAdminById()
        elif choice2==2:
            AdminService.GetAdminByUsername()
        elif choice2==3:
            AdminService.RegisterAdmin()
        elif choice2==4:
            AdminService.UpdateAdminInfo()
        elif choice2==5:
            AdminService.DeleteAdmin()
        else:
            return 

show_menu()


