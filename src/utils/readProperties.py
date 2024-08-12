'''
import configparser
import os
import yaml

# load the config.ini file
config = configparser.RawConfigParser()
config.read("src\\Configurations\\config.ini")

# load the browserstack.yaml file


class ReadConfig:

    @staticmethod
    def get_appium_server_url():
        appium_server_url = config.get('common info', 'appium_server_url')
        return appium_server_url

    @staticmethod
    def get_app_package():
        app_package = config.get('common info', 'appPackage')
        return app_package

    @staticmethod
    def get_app_activity():
        app_activity = config.get('common info', 'appActivity')
        return app_activity

    @staticmethod
    def get_no_reset():
        no_reset = config.getboolean('common info', 'True')
        return no_reset

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    # browser stack capabilities
    # Load the YAML file
    yaml_file_path = os.path.join(os.path.dirname(__file__), '../configurations/browserstack.yml')
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)'''

import configparser
import yaml
import os

class ReadConfig:
    def __init__(self):
        # Load the config.ini file
        config_ini_path = os.path.join(os.path.dirname(__file__), '../configurations/config.ini')
        self.config_ini = configparser.ConfigParser()
        self.config_ini.read(config_ini_path)

        # Load the browserstack.yml file
        yaml_file_path = os.path.join(os.path.dirname(__file__), '../browserstack.yml')
        with open(yaml_file_path, 'r') as file:
            self.config_yaml = yaml.safe_load(file)

    # Methods to access data from config.ini
    def get_password(self):
        return self.config_ini.get('common info', 'password')

    def get_appium_server_url(self):
        return self.config_ini.get('common info', 'appium_server_url')

    def get_app_activity(self):
        return self.config_ini.get('common info', 'appActivity')

    def get_app_package(self):
        return self.config_ini.get('common info', 'appPackage')

    def get_no_reset(self):
        return self.config_ini.getboolean('common info', 'noReset')

    # Methods to access data from browserstack.yml
    def get_user_name(self):
        return self.config_yaml['userName']

    def get_access_key(self):
        return self.config_yaml['accessKey']

    def get_app_url(self):
        return self.config_yaml['app']

    def get_browserstack_local(self):
        return self.config_yaml['browserstackLocal']

    def get_build_name(self):
        return self.config_yaml['buildName']

    def get_project_name(self):
        return self.config_yaml['projectName']

    def get_device_capabilities(self, device_index=0):
        """Retrieve the capabilities for the device at the specified index."""
        platform = self.config_yaml['platforms'][device_index]
        capabilities = {
            'platformName': platform['platformName'],
            'deviceName': platform['deviceName'],
            'platformVersion': platform['platformVersion'],
            'app': self.get_app_url(),
            'browserstack.user': self.get_user_name(),
            'browserstack.key': self.get_access_key(),
            'project': self.get_project_name(),
            'build': self.get_build_name(),
            'browserstack.local': self.get_browserstack_local(),
        }
        return capabilities
