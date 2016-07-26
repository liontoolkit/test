from MyModule import MyModule
import unittest

class TestMyModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = MyModule()

    def setUp(self):
        self.obj = self.__class__.obj

    def test___init__(self):
        with self.subTest(i=1):
            self.assertEqual(self.obj.number1,1)
        with self.subTest(i=2):
            self.assertEqual(self.obj.number2,2)

    def test_my_function(self):
        with self.subTest(i=1):
            self.assertEqual(self.obj.my_function(),self.obj.number1 + self.obj.number2)
        with self.subTest(i=2):
            self.assertEqual(self.obj.my_function(3,4),7)
        with self.subTest(i=3):
            self.assertEqual(self.obj.my_function(num1=5),5 + self.obj.number2)
        with self.subTest(i=4):
            self.assertEqual(self.obj.my_function(num2=3),self.obj.number1 + 3)
        with self.subTest(i=5):
            self.assertEqual(self.obj.my_function(10,-5),5)
        with self.subTest(i=6):
            self.assertEqual(self.obj.my_function(-10,-5),-15)

    def tearDown(self):
        self.obj = None

    @classmethod
    def tearDownClass(cls):
        del cls.obj

if __name__ == '__main__':
    unittest.main()