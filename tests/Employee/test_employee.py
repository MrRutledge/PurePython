# courtesy of Cory Shafer's youtube series
import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    #Using class methods
    @classmethod
    def setUpClass(cls):
        pass
    #teardown
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.emp_1 = Employee('Jane', 'Mark', 23098)
        self.emp_2 = Employee('Sue', 'Kim', 7809)
    def tearDown(self):
        pass 


    """Test the Employee class"""
    def test_email(self):
        # emp_1 = Employee('Jane','Mark',23098)
        # self.emp_2 = Employee('Sue','Kim',7809)

        self.assertEqual(self.emp_1.email,'Jane.Mark@email.com')
        self.assertEqual(self.emp_2.email,'Sue.Kim@email.com')

        self.emp_1.first = 'Dave'
        self.emp_2.first = 'Vue'

        self.assertEqual(self.emp_1.email,'Dave.Mark@email.com')
        self.assertEqual(self.emp_2.email, 'Vue.Kim@email.com')

    def test_fullname(self):
        """Testing Fullname function"""

        # self.emp_1 = Employee('Jane', 'Mark', 23098)
        # self.emp_2 = Employee('Sue', 'Kim', 7809)

        self.assertEqual(self.emp_1.fullname,'Jane Mark')
        self.assertEqual(self.emp_2.fullname,'Sue Kim')

        self.emp_1.last = 'Deer'
        self.emp_2.last = 'Jes'

        self.assertEqual(self.emp_1.fullname,'Jane Deer')
        self.assertEqual(self.emp_2.fullname,'Sue Jes')

    def test_apply_raise(self):
        """Testing the Pay Raise function"""

        # self.emp_1 = Employee('Jane','Mark',24000)
        # self.emp_2 = Employee('Lloyd','Jack',34000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,24252)
        self.assertEqual(self.emp_2.pay, 8199)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Mark/June')
            self.assertEqual(schedule,'Success!')

            mocked_get.return_value.ok = False
           # mocked_get.return_value.text = 'Success!'

            schedule = self.emp_2.monthly_schedule('July')
            mocked_get.assert_called_with('http://company.com/Kim/July')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()
