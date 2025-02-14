import unittest
import mymodule

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
                self.assertEqual((1 + 2), 3)
    def testAdd1(self):
                self.assertEqual(0 + 1, 1)
    def testAdd1(self):
                self.assertEqual(mymodule.total1(10,20),30)
    def testMultiply(self):
                self.assertEqual((0 * 10), 0)
                self.assertEqual((5 * 8), 40)
 
if __name__ == '__main__':
            unittest.main()
 

 #Dont write more than one text case inside one function.