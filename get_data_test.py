import unittest
import get_data

class test_get_data(unittest.TestCase):

    def test_user(self):
        self.assertIsNotNone(get_data.get_real_user)