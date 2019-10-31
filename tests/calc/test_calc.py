import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-10, 5), -5) #edge caases
        self.assertEqual(calc.add(-10, -5), -15)#edge cases

    #def test_sub(self):
     #   self.assertEqual(calc.sub(10, 5), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-10, 5), -15)  # edge caases
        self.assertEqual(calc.sub(-10, -5), -5)  # edge cases

    def test_mult(self):
        self.assertEqual(calc.mult(10, 5), 50)
        self.assertEqual(calc.mult(-1, 5), -5)  # edge caases
        self.assertEqual(calc.mult(-5, -3), 15)  # edge cases
    
    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-2, 2), -1)  # edge caases
        self.assertEqual(calc.div(-15, -3), 5)  # edge cases

        #self.assertRaises(ValueError, calc.div,10,2 )
        # context manager
        with self.assertRaises(ValueError): calc.div(10,0)

if __name__ == '__main__':
    unittest.main()
