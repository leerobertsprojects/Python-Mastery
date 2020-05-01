import unittest
import prog

class TestMain(unittest.TestCase):
    def setUp(self):
        print('Setting up files')

    def test_do_stuff(self):
        num = 10
        result = prog.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dhaksdhkjs'
        result = prog.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_def_stuff3(self):
        test_param = None
        result = prog.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print('Tearing down')

if __name__ == '__main__':
    unittest.main()









