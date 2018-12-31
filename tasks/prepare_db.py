import pathlib
import json
import sys
sys.path.append('.')
from xviewer.database import create_database
from utils import get_labels


CONFIG_PATH = pathlib.Path(__file__).parents[1].resolve()
config = CONFIG_PATH / 'config.json'


config = json.load(config.open())

_, filenames, _ = get_labels(config["labelfilename"])
print(set(filenames))
