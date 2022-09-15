import pytest
import unittest
from core.web.pages.LoginPage import LoginPage


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.loginpage = LoginPage()

    def test_search_in_python_org(self):
        self.loginpage.login_admin_page()

    def tearDown(self):
        self.loginpage.close()


if __name__ == "__main__":
    unittest.main()
