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

if __name__ =="__main__":
    unittest.main()
