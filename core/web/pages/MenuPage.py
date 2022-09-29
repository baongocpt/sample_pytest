from core.web.base.BasePage import BasePage


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_page_locators = self.locators["menu"]

    def navigate_to_posts(self):
        self.element_click(
            locator=self.menu_page_locators['posts']["locator"],
            locator_type=self.menu_page_locators['posts']["locator_type"])
