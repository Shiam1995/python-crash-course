import unittest

from exercise_11_3 import employee

class test_employee(unittest.TestCase):

    def setUp(self):
        self.employee = employee("ann", 'lee', 30000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 35000)

    def give_customer_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 31000)


unittest.main()