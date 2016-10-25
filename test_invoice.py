import unittest
import invoice

class InvoiceCalculatorTests(unittest.TestCase):
    
    def test_divided_correctly(self):
        result = invoice.divide_pay(360, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}) #execute function with given input
        expected_result = {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0} #expected results for given input
        print("{} = {}".format(result, expected_result))
                
    def test_correct_decimal_hours(self):
        result = invoice.divide_pay(360, {"Alice": 3.5, "Bob": 3.5, "Carol": 6.5}) #execute function with given input
        expected_result = {"Alice": 93.0, "Bob": 93.0, "Carol": 173.0} #expected results for given input
        for key in result: 
            if not self.assertEqual(round(result[key]), (expected_result[key])): 
                print("pass: {} rounded = {}".format((result[key]), (expected_result[key])))
                
    def test_correct_decimal_pay(self):
        result = invoice.divide_pay(150.50, {"Alice": 3.5, "Bob": 3.5, "Carol": 6.5}) #execute function with given input
        expected_result = {"Alice": 39.0, "Bob": 39.0, "Carol": 72.0} #expected results for given input
        for key in result: 
            if not self.assertEqual(round(result[key]), (expected_result[key])): 
                print("pass: {} rounded = {}".format((result[key]), (expected_result[key])))
                
    def test_zero_hour_person(self):
        pay = invoice.divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
        if not self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0}) :
            print("pass: {} = {}".format(pay, ({"Alice": 120.0, "Bob": 240.0, "Carol": 0.0})))
            
    def test_negative_value_hrs(self):
        with self.assertRaises(ValueError):
            pay = invoice.divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": -12.0})
        print("Value Error raised as expected")
        
            
    def test_zero_hours_total(self):
        with self.assertRaises(ValueError):
           invoice.divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
        print("Value Error raised as expected")
           
    def test_no_people(self):
        with self.assertRaises(ValueError):
            pay = invoice.divide_pay(360.0, {})
        print("Value Error raised as expected")
        
    def test_invalid_hrs_non_numeric(self):
        with self.assertRaises(ValueError):
            pay = invoice.divide_pay(360.0, {"Alice": float("a"), "Bob": 6.0, "Carol": 0.0})
        print("Value Error raised as expected")

if __name__ == "__main__":
    unittest.main()