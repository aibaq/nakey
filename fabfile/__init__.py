from . import common
from . import install

from fabric.decorators import task
from fabric.state import env
from dotenv import load_dotenv

import os

load_dotenv()

env.repository = "https://github.com/aibaq/nakey"
env.repository_ssh = "git@github.com:aibaq/nakey"
env.repo_name = "nakey"
env.hosts = ["api.nakey.kz"]


@task
def dev():
    env.config = 'Dev'
    env.user = os.getenv('DEV_USER')
    env.password = os.getenv('DEV_PASSWORD')
    env.hosts = [os.getenv('DEV_HOST')]
    env.environ = 'dev'
    env.dotenv_path = '{}/.env'.format(env.repo_name)


@task
def prod():
    env.config = 'Prod'
    env.user = os.getenv('PROD_USER')
    env.password = os.getenv('PROD_PASSWORD')
    env.hosts = [os.getenv('PROD_HOST')]
    env.environ = 'prod'
    env.dotenv_path = '{}/.env'.format(env.repo_name)
    env.port = 21111
