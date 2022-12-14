from configparser import ConfigParser
import os

config = ConfigParser()

config["PATH"] = {
    'ROOT_DIR': os.path.dirname(os.path.realpath(__file__))
}

config['CLEAR'] = {
    'Windows':'cls',
    'Linux':'clear',
}

with open('config.ini', 'w') as f:
    config.write(f)