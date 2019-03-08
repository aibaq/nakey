from fabric.decorators import task
from fabric.operations import get, run, sudo
from fabric.state import env
from fabric.context_managers import shell_env
from functools import wraps

import dotenv


def set_env():
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with shell_env(DJANGO_CONFIGURATION=env.config, USER=env.user):
                run("echo $DJANGO_CONFIGURATION, $USER test")
                return func(*args, **kwargs)
        return inner
    return decorator



@task
def config(action=None, key=None, value=None):
    '''Manage project configuration via .env

    e.g: fab config:set,<key>,<value>
         fab config:get,<key>
         fab config:unset,<key>
         fab config:list
    '''
    run('touch %(dotenv_path)s' % env)
    command = dotenv.get_cli_string(env.dotenv_path, action, key, value)
    run('source ~/envs/{}/bin/activate; '.format(env.repo_name) + command)


@task
@set_env()
def gunicorn_logs():
    run("tail -f /var/log/gunicorn/nakey.log")


@task
@set_env()
def celery_logs():
    run("tail -f /var/log/celery/nakey.log")

@task
@set_env()
def compile_messages():
    run("cd ~; source ./envs/nakey/bin/activate; "
        "cd ~/{}/; django-admin compilemessages".format(env.repo_name))

@task
@set_env()
def git_pull():
    """
    """
    run("cd ~/{}/; git pull".format(env.repo_name))


@task
@set_env()
def build_front():
    """
    """
    run("cd ~/{}/front/; npm install; npm run build;".format(env.repo_name))


@task
@set_env()
def update_supervisor():
    sudo("cp -r ~/{0}/configs/supervisor/{1}/* /etc/supervisor/conf.d".format(env.repo_name, env.environ))
    sudo("""supervisorctl reread;
            supervisorctl restart {0};
            supervisorctl restart celery;
            supervisorctl update;
            supervisorctl status;
        """.format(env.repo_name))


@task
@set_env()
def update_nginx(first_run=0):
    sudo("cp ~/{0}/configs/nginx/{1}/*.conf /etc/nginx/sites-available".format(env.repo_name, env.environ))
    if first_run:
        sudo("ln -s /etc/nginx/sites-available/{0}.conf /etc/nginx/sites-enabled/{0}.conf".format(env.repo_name))
    sudo("service nginx restart")


@task
@set_env()
def restart():
    run("cd ~/{} && . ./run.sh".format(env.repo_name))
    update_supervisor()
    update_nginx()


@task
@set_env()
def letsencrypt(config_name, *domains):
    '''
    usage: fab env common.first_run:config_name,domain1.com,domain2.com
    '''
    domains = list(domains)
    domains_command = " ".join(["-d " + domain for domain in domains])
    sudo("service nginx stop")
    run("mkdir -p ~/letsencrypt;mkdir -p ~/letsencrypt/work;mkdir -p ~/letsencrypt/logs;mkdir -p ~/letsencrypt/cron;")
    sudo(("certbot certonly -n --expand --work-dir ~/letsencrypt/work/ --logs-dir ~/letsencrypt/logs/ " + domains_command).format(env.repo_name, config_name))
    run("openssl dhparam -out ~/{0}/configs/letsencrypt/{1}/ssl-dhparams.pem 2048".format(env.repo_name, config_name)).format(env.repo_name, env.repository_ssh)
    run("echo \" 0 9 1,15 * * ~/letsencrypt/cron/cronscript.sh\" > ~/letsencrypt/cron/crontab")
    run("""
        echo \"
        sudo service nginx stop;
        certbot renew -n --config-dir ~/{0}/configs/letsencrypt/ --work-dir ~/letsencrypt/work/ --logs-dir ~/letsencrypt/logs/;
        chmod -R 775 ~/{0}/configs/letsencrypt/;
        sudo service nginx start;
        \" > ~/letsencrypt/cron/cronscript.sh
        """.format(env.repo_name, env.repository_ssh))
    run("chmod +x ~/letsencrypt/cron/cronscript.sh")
    run("crontab ~/letsencrypt/cron/crontab")
    update_nginx()
