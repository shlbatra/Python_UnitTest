import unittest
from Python_NamedFunction import formatted_name

class NamesTestCase(unittest.TestCase):

    def setUp(self):
        print("Setup called")
        self.first_name="Sahil"
        self.middle_name="Awesome"
        self.last_name="Batra"

    def test_first_last_name(self):
        print("Test1 Called")
        result=formatted_name(self.first_name,self.last_name)
        self.assertEqual(result,"Sahil Batra")

    def test_first_middle_name(self):
        print("Test2 Called")
        result=formatted_name(self.first_name,self.last_name,self.middle_name)
        self.assertEqual(result,"Sahil Awesome Batra")

    def tearDown(self):
        print("TearDown Called")
        self.first_name=""
        self.middle_name=""
        self.last_name=""


unittest.main()
