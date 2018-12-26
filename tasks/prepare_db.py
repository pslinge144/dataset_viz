import pathlib
import json
import sys
sys.path.insert(0, '.')
from server.server.create_database import create_database


CONFIG_FILE = pathlib.Path(__file__).parents[1].resolve() / 'config.json'


config = json.load(CONFIG_FILE)

print(config)
