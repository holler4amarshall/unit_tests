import unittest
import invoice

class InvoiceCalculatorTests(unittest.TestCase):
    
    def test_divided_correctly(self):
        result = invoice.divide_pay(360, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
        expected_result = {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0}
        print(result)
        for key in result: 
            self.assertEqual((result[key]), (expected_result[key]))

if __name__ == "__main__":
    unittest.main()