from configparser import ConfigParser


class ConfigSingleton(object):
    config = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self.config is None:
            self.mode = None
            self.config = ConfigParser()
            self.a = self.config.read('config.ini')

    def get_config(self, section: str, key: str) -> str:
        return self.config.get(section, key)

    def reload_configs(self):
        self.config = ConfigParser()
        self.config.read('config.ini')
