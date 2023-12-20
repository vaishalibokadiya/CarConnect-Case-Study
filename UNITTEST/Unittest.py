import unittest

import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/DAO')

from CustomerService import CustomerService
from VehicleService import VehicleService


class myTestCase(unittest.TestCase):
    def testCustomerUpdate(self):
        isUpdated=CustomerService.UpdateCustomer()
        
        self.assertTrue(isUpdated)

    def testAddVehicle(self):
        isAdded=VehicleService.AddVehicle()

        self.assertTrue(isAdded)

    def testUpdateVehicle(self):
        isUpdated=VehicleService.UpdateVehicle()

        self.assertTrue(isUpdated)

    def testListAllAvailableVehicle(self):
        isListed=VehicleService.testListAllAvailableVehicle()

        self.assertTrue(isListed)

    def testListAllVehicle(self):
        isListed=VehicleService.testListAllVehicle()

        self.assertTrue(isListed)
    

if __name__ =="__main__":
    unittest.main()
