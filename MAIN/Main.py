import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/DAO')
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/UTIL')

from CustomerService import CustomerService
from ReservationService import ReservationService
from VehicleService import VehicleService
from AdminService import AdminService

from Util import DBConnUtil,DBPropertyUtil

# Main Menu function
def show_menu():
    try:
        [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
    except:
        print("Error in connection")
    else:
        choice=0
        while(choice<5):
            print("=======================================")
            print("1: Customer Services")
            print("2: Vehicle Services")
            print("3: Reservation Services")
            print("4: Admin Services")
            print("5: Exit")
            print("=======================================")
            choice=int(input("Enter your choice: "))

            if choice==1:
                print("=======================================")
                print("1: Get customer by id")
                print("2: Get customer by username")
                print("3: Register customer")
                print("4: Update customer information")
                print("5: Delete customer")
                print("=======================================")
                choice2=int(input("Enter your choice: "))
                if choice2==1:
                    CustomerService.GetCustomerById(mycursor,mydb)
                elif choice2==2:
                    CustomerService.GetCustomerByUsername(mycursor,mydb)
                elif choice2==3:
                    CustomerService.RegisterCustomer(mycursor,mydb)
                elif choice2==4:
                    CustomerService.UpdateCustomer(mycursor,mydb)
                elif choice2==5:
                    CustomerService.DeleteCustomer(mycursor,mydb)
                else:
                    pass

            elif choice==2:
                print("=======================================")
                print("1: Get vehicle by id")
                print("2: Get available vehicles")
                print("3: Add vehicle")
                print("4: Update vehicle")
                print("5: Remove vehicle")
                print("=======================================")
                choice2=int(input("Enter your choice: "))
                if choice2==1:
                    VehicleService.GetVehicleById(mycursor,mydb)
                elif choice2==2:
                    VehicleService.GetAvailableVehicles(mycursor,mydb)
                elif choice2==3:
                    VehicleService.AddVehicle(mycursor,mydb)
                elif choice2==4:
                    VehicleService.UpdateVehicle(mycursor,mydb)
                elif choice2==5:
                    VehicleService.RemoveVehicle(mycursor,mydb)
                else:
                    pass 

            elif choice==3:
                print("=======================================")
                print("1: Get reservation by id")
                print("2: Get reservation by customer id")
                print("3: Create reservation")
                print("4: Update reservation")
                print("5: Cancel reservation")
                print("=======================================")

                choice2=int(input("Enter your choice: "))
                if choice2==1:
                    ReservationService.GetReservationById(mycursor,mydb)
                elif choice2==2:
                    ReservationService.GetReservationsByCustomerId(mycursor,mydb)
                elif choice2==3:
                    ReservationService.CreateReservation(mycursor,mydb)
                elif choice2==4:
                    ReservationService.UpdateReservation(mycursor,mydb)
                elif choice2==5:
                    ReservationService.CancelReservation(mycursor,mydb)
                else:
                    pass 


            elif choice==4:
                print("=======================================")
                print("1: Get admin by id")
                print("2: Get admin by username")
                print("3: Register admin")
                print("4: Update admin information")
                print("5: Delete admin")
                print("=======================================")
                choice2=int(input("Enter your choice: "))
                if choice2==1:
                    AdminService.GetAdminById(mycursor,mydb)
                elif choice2==2:
                    AdminService.GetAdminByUsername(mycursor,mydb)
                elif choice2==3:
                    AdminService.RegisterAdmin(mycursor,mydb)
                elif choice2==4:
                    AdminService.UpdateAdmin(mycursor,mydb)
                elif choice2==5:
                    AdminService.DeleteAdmin(mycursor,mydb)
                else:
                    pass 
                
            else:
                mydb.close()

show_menu()
