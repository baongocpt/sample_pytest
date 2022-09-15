from util.load_settings import Settings
from core.web.base.BasePage import BasePage
from time import sleep


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.settings = Settings().json_content

    def login_admin_page(self):
        wpadmin_url = self.settings["url"]["base_url"] + self.settings["url"]["admin_url"]
        self.goto(wpadmin_url)
        self.send_keys(self.settings["accounts"]["admin_usr"], locator="user_login")
        self.send_keys(self.settings["accounts"]["admin_pwd"], locator="user_pass")
        self.get
        sleep(3)

