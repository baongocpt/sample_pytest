from time import sleep

import pytest
import unittest
from core.web.pages.LoginPage import LoginPage
from core.web.pages.MenuPage import MenuPage
from core.web.pages.PostsPage import PostsPage


@pytest.mark.usefixtures("oneTimeSetup")
class TestHomePage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.loginpage = LoginPage(self.driver)
        self.menupage = MenuPage(self.driver)
        self.postspage = PostsPage(self.driver)

    def test_login_successfully(self):
        self.loginpage.login_admin_page()
        self.menupage.navigate_to_posts()
        post_name = "Test sponsor"
        self.postspage.search_post(post_name)
        self.postspage.verify_post_displayed_in_all_posts(post_name)


if __name__ == "__main__":
    unittest.main()
