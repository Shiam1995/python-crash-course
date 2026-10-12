import unittest

from exercise_11_2 import give_me_info

class test_population(unittest.TestCase):

    def test_give_me_info(self):
        formatted_name = give_me_info('London', 'England')
        self.assertEqual(formatted_name,'England : London')

    def test_give_me_info_full(self):
        formatted_name = give_me_info('London', 'England', '100000')
        self.assertEqual(formatted_name,'England : London - 100000')


unittest.main()