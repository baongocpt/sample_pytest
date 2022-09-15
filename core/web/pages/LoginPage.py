from core.web.base.BasePage import BasePage
from time import sleep


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.login_page_locators = self.locators["login_page"]

    def login_admin_page(self):
        wpadmin_url = self.settings["url"]["base_url"] + self.settings["url"]["admin_url"]
        self.goto(wpadmin_url)
        self.send_keys(self.settings["accounts"]["admin_usr"],
                       locator=self.login_page_locators['ipt_username']["locator"],
                       locator_type=self.login_page_locators['ipt_username']["locator_type"])
        self.send_keys(self.settings["accounts"]["admin_pwd"],
                       locator=self.login_page_locators['ipt_password']["locator"],
                       locator_type=self.login_page_locators['ipt_password']["locator_type"])
        self.element_click(locator=self.login_page_locators['btn_submit']["locator"],
                           locator_type=self.login_page_locators['btn_submit']["locator_type"])
        print(self.get_title())
        sleep(3)

