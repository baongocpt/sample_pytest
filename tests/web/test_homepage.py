import pytest
import unittest
from core.web.pages.LoginPage import LoginPage
from core.web.pages.MenuPage import MenuPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)

    def test_login_successfully(self):
        self.loginpage.login_admin_page()
        self.menupage.navigate_to_posts()


if __name__ == "__main__":
    unittest.main()
