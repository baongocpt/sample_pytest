import pytest
import unittest
from core.web.pages.LoginPage import LoginPage


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.loginpage = LoginPage()

    def test_login_successfully(self):
        self.loginpage.login_admin_page()

    def tearDown(self):
        self.loginpage.close()


if __name__ == "__main__":
    unittest.main()
