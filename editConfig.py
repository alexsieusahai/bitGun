import subprocess

from config import config

def editConfig():
    subprocess.call([config['favEditor'],'config.yml'])
