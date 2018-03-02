import unittest


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("wakanda", "user", "12345today", "11:45")

    def tearDown(self):
        del self.user

    def test_create_user(self):
        self.assertTrue(self.user.create_user(), "User successfully created")


class CommentsTestCase(unittest.TestCase):
    def setUp(self):
        self.comment = Comments("wakanda", "user", "12345today", "11:45", "This is a comment")

    def tearDown(self):
        del self.comment

    def test_create_comment(self):
        self.assertTrue(self.comment.create_comment(), "Comment successfully created")


if __name__ == '__main__':
    unittest.main()
