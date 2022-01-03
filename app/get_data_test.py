import unittest
import get_data

class test_get_data(unittest.TestCase):

    def test_user(self):
        self.assertIsNotNone(get_data.get_named_user("JDeasley"))

    # def test_user_dict(self):
    #     usr1 = get_data.get_named_user("JDeasley")
    #     usr2 = get_data.get_named_user("not_a_real_user")

    #     dct1 = get_data.create_user_dict(usr1)
    #     dct2 = get_data.create_user_dict(usr2)

    #     self.assertIsNotNone(dct1)
    #     self.assertIsNone(dct2)

    #     for _, v in dict(dct1).items():
    #         self.assertIsNotNone(v)

    def test_repo(self):
        repo1 = get_data.get_named_repo("JDeasley/Measuring_SWENG_Visualisation")
        repo2 = get_data.get_named_repo("not_a_real_user/fake_repo")

        self.assertIsNotNone(repo1)
        self.assertIsNone(repo2)

    # def test_repo_dict(self):
    #     repo1 = get_data.get_named_repo("JDeasley/Measuring_SWENG_Visualisation")
    #     repo2 = get_data.get_named_repo("not_a_real_user/fake_repo")

    #     dct1 = get_data.create_repo_dict(repo1)
    #     dct2 = get_data.create_repo_dict(repo2)

    #     self.assertIsNotNone(dct1)
    #     self.assertIsNone(dct2)

    #     for _, v in dict(dct1).items():
    #         self.assertIsNotNone(v)

    def test_top_contributors(self):
        # repo1 = get_data.get_named_repo("JDeasley/Measuring_SWENG_Visualisation")
        # repo2 = get_data.get_named_repo("not_a_real_user/fake_repo")

        cons1 = get_data.get_top_contributors("JDeasley/Measuring_SWENG_Visualisation")
        self.assertRaises(AttributeError, get_data.get_top_contributors, "not_a_real_user/fake_repo")
        # cons2 = get_data.get_top_contributors("not_a_real_user/fake_repo")

        self.assertNotEqual([], cons1)
        
        count = 0

        for _ in cons1:
            count += 1

        self.assertEquals(1, count)
        self.assertEquals("JDeasley", cons1[0].login)

    def test_users_commits(self):
        user1 = get_data.get_named_user("JDeasley")
        commits1 = get_data.get_users_commits(user1)
        
        # 434433749 is the id of the repo containing this project
        self.assertTrue(434433749 in commits1.keys())
        # 2325298 is the id of the "torvalds/linux" repo, which I have never contributed to.
        self.assertFalse(2325298 in commits1.keys())

    def test_user_file_count(self):
        user1 = get_data.get_named_user("JDeasley")
        files1 = get_data.get_user_file_count(user1)

        # I have commited a few Python files to GitHub
        self.assertTrue("py" in files1.keys())
        self.assertGreaterEqual(files1.get("py"), 3)
        # I have never commited C files to GitHub
        self.assertFalse("c" in files1.keys())

        