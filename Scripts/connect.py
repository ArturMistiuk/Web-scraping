import configparser
import os
from pathlib import Path

from mongoengine import connect

CURRENT_DIR = Path.cwd()
PATH_TO_LIB = os.path.join(CURRENT_DIR, '../Lib/')
CONFIG_PATH = os.path.join(CURRENT_DIR, '../Lib/config.ini')

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
# connect to cluster on AtlasDB with connection string

connection = connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)
