import json


class Settings:
    def __init__(self):
        self.json_file_obj = open('../conf/settings.json')
        self.json_content = json.load(self.json_file_obj)
