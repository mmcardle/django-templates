## Django Template

Django templates using docker compose

### Template 1

Simple Django app in a single docker container

    cd template1
    docker-compose build
    docker-compose up

### Template 2

Simple Django app in a single docker container with nginx, uwsgi and circusd.

    cd template2
    docker-compose build
    docker-compose up

### Template 3

Simple Django app in multi docker containers
Webapp container uses nginx, uwsgi and circusd.
Other containers are a Postgres Database container and a Redis cache container.

##### Commands

    cd template3
    docker-compose build
    docker-compose up

in another terminal, create an admin user.

    docker-compose exec webapp python3 /project/manage.py createsuperuser

Now login and add some more users to the database with the user at http://127.0.0.1:8000/admin/

Test out the cache at http://127.0.0.1:8000/
