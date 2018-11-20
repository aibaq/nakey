#!/usr/bin/env bash
createdb nakey;
psql -c "create user nakey with password 'nakey'";
psql -c 'grant all privileges on database nakey to nakey';
sudo rabbitmqctl add_user nakey nakey
sudo rabbitmqctl add_vhost nakey
sudo rabbitmqctl set_user_tags nakey nakey_tag
sudo rabbitmqctl set_permissions -p nakey nakey ".*" ".*" ".*"
mkdir logs;