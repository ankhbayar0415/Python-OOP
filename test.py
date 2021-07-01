import unittest

from Bikes import Bikes
from MountainBikes import MountainBikes
from CityBikes import CityBikes
from ElectricBikes import ElectricBikes
from Users import Users

class TestBikeRentals(unittest.TestCase):

    def setUp(self):
        self.obj1 = MountainBikes("typ  e", "name", "description", 15, 10, 10, 1)  
        self.obj2 = ElectricBikes("type", "name", "description", 15, 10, 3)  
        self.obj3 = CityBikes("type", "name", "description", 15, 10, 10, 5)  

    def test_getDiscount(self):
        self.assertEqual(self.obj1.getDiscount(), 10)
        self.assertEqual(self.obj3.getDiscount(), 10)
    def test_getInsurance(self):
        self.assertEqual(self.obj2.getInsurance(), 3)
    def test_getHour(self):
        self.assertEqual(self.obj1.getHour(), 1) 
        self.assertEqual(self.obj3.getDiscount(), 10)
    def test_getEffectivePrice(self):
        self.assertEqual(self.obj1.getEffectivePrice(2, 1), 18) 
        self.assertEqual(self.obj2.getEffectivePrice(1, 1), 13) 
        self.assertEqual(self.obj3.getEffectivePrice(1, 1), 5) 
    def test_rent_negative_number_of_bikes(self):
        self.assertEqual(self.obj1.getEffectivePrice(1, -1), 0)
    def test_rent_valid_number_of_bikes(self):
        self.assertEqual(self.obj1.getEffectivePrice(1, 1), 9)
    def test_rent_zero_number_of_bikes(self):
        self.assertEqual(self.obj2.getEffectivePrice(1, 0), 0)    
    def test_rent_for_invalid_positive_number_of_bikes(self):
        self.assertEqual(self.obj2.getEffectivePrice(1, 16), 0)

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user1 = Users("full name", "user id", "password", 122.5, "Canondale for 5 hours.") 
    
    def test_get_bill(self):
        self.assertEqual(self.user1.getBill(), 122.5)  
    def test_set_bill(self):
        self.user1.setBill(100)
        self.assertEqual(self.user1.bill, 222.5)
    def test_get_user_id(self):
        self.assertEqual(self.user1.getUserID(), "user id")
    def test_get_password(self):
        self.assertEqual(self.user1.getPassword(), "password")
    def test_get_rental_details(self):
        self.assertEqual(self.user1.getRentalDetails(), "Canondale for 5 hours.")
    def test_set_rental_details(self):
        self.user1.setRentalDetails("Canondale for 4 hours.")
        self.assertEqual(self.user1.rental_details, "Canondale for 5 hours.Canondale for 4 hours.")
    

if __name__ == '__main__':
    unittest.main()