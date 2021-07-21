import json
from os import error
import os


class Config:
    
    _config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config.json')

    def __init__(self) -> None:
        self.load()
        self.validateConfig()
        pass

    def load(self):
        file = open(self._config_path, 'r')
        self.config = json.load(file)


    def validateConfig(self):
        #TODO: implement
        pass

    def validateType(self, entry):
        #TODO: implement
        pass

    def get(self, attribute:str):
        res = self.config[attribute]
        if(not res):
            raise KeyError(f'No entry found in the Config for the attribute {attribute}')
        self.validateType(res)
        return res