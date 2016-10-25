import unittest
import invoice

class InvoiceCalculatorTests(unittest.TestCase):
    
    def test_divided_correctly(self):
        result = invoice.divide_pay(360, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}) #execute function with given input
        expected_result = {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0} #expected results for given input
        for key in result: 
            if not self.assertEqual((result[key]), (expected_result[key])): 
                print("pass: {} = {}".format((result[key]), (expected_result[key])))
                
                
    def test_zero_hour_person(self):
        pay = invoice.divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
        if not self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0}) :
            print("pass: {} = {}".format(pay, ({"Alice": 120.0, "Bob": 240.0, "Carol": 0.0})))
            
    def test_zero_hours_total(self):
       with self.assertRaises(ValueError):
           invoice.divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
        

if __name__ == "__main__":
    unittest.main()