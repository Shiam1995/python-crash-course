import unittest

from exercise_11_1 import give_me_info

class testCity(unittest.TestCase):
    def test_give_me_info(self):
        formatted_name = give_me_info('london', 'england')
        self.assertEqual(formatted_name,'england : london')

unittest.main()