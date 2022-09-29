import json


class Settings:
    def __init__(self):
        self.general_settings_file_obj = open('../../conf/general_settings.json')
        self.general_settings = json.load(self.general_settings_file_obj)
        self.settings_file_obj = open('../../conf/%s_settings.json' % self.general_settings["page_under_test"])
        self.settings = json.load(self.settings_file_obj)
        self.locators_file_obj = open('../../conf/%s_locators.json' % self.general_settings["page_under_test"])
        self.locators = json.load(self.locators_file_obj)
