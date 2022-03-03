import unittest
from employee import Employee

class TestGiveRaise(unittest.TestCase):
    """tests for employee.py"""
    def setUp(self):
        self.employee = Employee('Eric', 'Smith', 9000)
        self.custom_raise = 7000
        
    def test_give_default_raise(self):
        self.raised_salary = self.employee.give_raise()
        self.assertEqual(self.raised_salary, self.employee.annual_salary)

    def test_give_custom_raise(self):
        self.raised_salary = self.employee.give_raise(self.custom_raise)
        self.assertEqual(self.raised_salary, self.employee.annual_salary)

if __name__ == '__main__':
    unittest.main()

