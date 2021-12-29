import unittest
import get_data

class test_get_data(unittest.TestCase):

    def test_user(self):
        self.assertIsNotNone(get_data.get_user())

    def test_user_dict(self):
        usr1 = get_data.get_user()
        usr2 = get_data.get_fake_user("not_a_real_user")

        dct1 = get_data.create_user_dict(usr1)
        dct2 = get_data.create_user_dict(usr2)

        self.assertIsNotNone(dct1)
        self.assertIsNone(dct2)

        for _, v in dict(dct1).items():
            self.assertIsNotNone(v)

