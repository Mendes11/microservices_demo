# orders

## Setup

1. Create a python3 virtualenv, you can choose:

    * *WITH VIRTUALENVWRAPPER* (Recommended)
        * `mkvirtualev myvenv --python=python3`
        * `workon myvenv`

    * *WITHOUT VIRTUALENVWRAPPER*
        * `virtualenv myvenv --python=python3`
        * `source myvenv/bin/activate`

2. Install all Python Libraries Requirements

    * `pip install -r requirements.txt`

3. Install Postgres SQL and RabbitMQ
    * `sudo apt install postgresql rabbitmq-server` 

4. Create your Database:
    * *WITH POSTGRESQL*
        * `sudo -u postgres psql`
        * `CREATE ROLE <username> WITH ENCRYPTED PASSWORD '<password>' LOGIN
         CREATEDB;`
        * `CREATE DATABASE <db_name> owner <username>;`
        * `\q` to exit psql.

5. Execute all migrations: `python manage.py migrate`

## Running Django API
* `python manage.py runserver 127.0.0.1:[PORT]`

### Running Services
* `nameko run services.service --config=config.yaml`
