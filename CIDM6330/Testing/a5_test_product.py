import unittest
from product import Product

class TestProduct(unittest.TestCase):
    # def test_working(self):
    #    pass

    def test_transform_name_for_sku(self):
       
        # arrange
        small_black_shoes = Product("shoes", "S", "black")
        expected_value = "SHOES"
        # act
        actual_value = small_black_shoes.transform_name_for_sku()
        # assert
        self.assertEqual(expected_value, actual_value)
        
    
    def test_transform_color_for_sku(self):
       
        # arrange
        small_blue_shoes = Product("shoes", "S", "blue")
        expected_value = "BLUE"
        # act
        actual_value = small_blue_shoes.transform_color_for_sku()
        # assert
        self.assertEqual(expected_value, actual_value)