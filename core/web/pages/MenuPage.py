from core.web.base.BasePage import BasePage


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_page_locators = self.locators["menu"]

    def navigate_to(self, menu_name):
        self.element_click(
            locator=self.menu_page_locators[menu_name]["locator"],
            locator_type=self.menu_page_locators[menu_name]["locator_type"])

    def navigate_to_posts(self):
        self.navigate_to('posts')

    def navigate_to_pages(self):
        self.navigate_to('pages')

    def navigate_to_brands(self):
        self.navigate_to('brands')

    def navigate_to_products(self):
        self.navigate_to('products')

    def navigate_to_sweepstakes(self):
        self.navigate_to('sweepstakes')

    def navigate_to_media(self):
        self.navigate_to('media')

    def navigate_to_forms(self):
        self.navigate_to('forms')

    def navigate_to_pages(self):
        self.navigate_to('pages')
