import unittest
import user_interface 
from cans import Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel, Penny

class TestUserInterface(unittest.TestCase):
    
    def test_validate_main_menu(self):
        """Validating if passing 1, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(1)
        self.assertEqual(returned_value, (True, 1))

    def test_validate_main_menu_two(self):
        """Validating if passing 2, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(2)
        self.assertEqual(returned_value, (True, 2))

    def test_validate_main_menu_three(self):
        """Validating if passing 3, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(3)
        self.assertEqual(returned_value, (True, 3))

    def test_validate_main_menu_four(self):
        """Validating if passing 4, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(4)
        self.assertEqual(returned_value, (True, 4))    

    def test_validate_main_menu_b(self):
        """Validating if passing 5, fapple (False, None) will be returned"""
        returned_value = user_interface.validate_main_menu(5)
        self.assertEqual(returned_value, (False, None)) 

class TestTryParseInt(unittest.TestCase):

    def test_try_parse_int(self):
        """10 as a string goes in, needs to return int value 10"""
        returned_value = user_interface.try_parse_int('10')
        self.assertEqual(returned_value, 10)
        pass

    def test_try_parse_int_b(self):
        """'hello' goes in, needs to return 0"""
        returned_value = user_interface.try_parse_int('hello')
        self.assertEqual(returned_value, 0)



if __name__ == "__main__":
    unittest.main()        