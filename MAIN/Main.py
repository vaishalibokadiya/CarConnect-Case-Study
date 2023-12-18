import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/Dao')

from DAO import CustomerService, ReservationService, VehicleService, AdminService

CustomerService.RegisterCustomer()
VehicleService.GetAvailableVehicles()
ReservationService.CreateReservation()
ReservationService.GetReservationsByCustomerId()
ReservationService.CancelReservation()
AdminService.RegisterAdmin()
VehicleService.GetAvailableVehicles()
AdminService.AddVehicle()
VehicleService.GetAvailableVehicles()
CustomerService.DeleteCustomer()