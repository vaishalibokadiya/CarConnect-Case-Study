import unittest

import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/DAO')

from CustomerService import CustomerService
from VehicleService import VehicleService

# Unit tests
class myTestCase(unittest.TestCase):
    # test for customer update
    def testCustomerUpdate(self):
        isUpdated=CustomerService.UpdateCustomer()
        
        self.assertTrue(isUpdated)

    # test for adding vehicle
    def testAddVehicle(self):
        isAdded=VehicleService.AddVehicle()

        self.assertTrue(isAdded)

    # test for updating vehicle
    def testUpdateVehicle(self):
        isUpdated=VehicleService.UpdateVehicle()

        self.assertTrue(isUpdated)

    # test for listing all available vehicles
    def testListAllAvailableVehicle(self):
        isListed=VehicleService.GetAvailableVehicles()

        self.assertTrue(isListed)  

if __name__ =="__main__":
    unittest.main()
