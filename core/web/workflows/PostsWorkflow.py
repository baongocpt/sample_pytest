from core.web.pages.PostsPage import PostsPage


class PostsWorkflow(PostsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_post(self, post_name):
        self.driver
