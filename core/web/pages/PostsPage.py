from core.web.base.BasePage import BasePage


class PostsPage(BasePage):
    def __init__(self, driver):
        super(PostsPage, self).__init__(driver)
        self.posts_page_locators = self.locators["posts"]

    def click_add_new_post(self):
        self.element_click(locator=self.posts_page_locators["add_new_btn"]["locator"],
                           locator_type=self.posts_page_locators["add_new_btn"]["locator_type"])

    def add_title(self, title):
        pass

    def add_paragraph_to_content(self, text):
        pass

    def search_post(self, post_name):
        self.send_keys(data=post_name,
                       locator=self.posts_page_locators["search_post_input"]["locator"],
                       locator_type=self.posts_page_locators["search_post_input"]["locator_type"])
        self.element_click(locator=self.posts_page_locators["search_post_btn"]["locator"],
                           locator_type=self.posts_page_locators["search_post_btn"]["locator_type"])

    def verify_post_displayed_in_all_posts(self, post_name):
        self.assert_element_present(selector=self.posts_page_locators["post_item"]["locator"] % post_name,
                                    by=self.posts_page_locators["post_item"]["locator_type"])
