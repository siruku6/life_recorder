[![CircleCI Status](https://circleci.com/gh/siruku6/life_recorder.svg?style=svg)](https://app.circleci.com/pipelines/github/siruku6/life_recorder?branch=master)

# life_recorder
display activity log

# Requirement

## Middlewares

- pipenv
- postgresql

---

**\*You don't have to setup these Middlewares in your OS, if you build your environment with docker and docker-compose !!**

# Development

## How to build development environment?
### With Docker

1. Execute following commands
    ```bash
    $ cp .env.example .env
    $ docker-compose build
    $ docker-compose up -d
    $ docker attach life_recorder_web_1
    $ docker-compose exec web python manage.py createsuperuser
    >> ** Input information of your superuser! **
    ```
1. Then, you can access to
    - `localhost:8000/admin`
    - `localhost:8000/cms`

1. You can run automated test by this command
    ```bash
    $ docker-compose exec web python manage.py test
    ```

### With python on your OS
1. Install and setup `pipenv` and `postgresql`
1. Prepare `.env`  
Copy from .env.example to .env, then rewrite it.
    ```bash
    $ cp .env.example .env
    $ vim .env
    ```
    |No|Name       |Value Example|Note                                   |
    |:-|:----------|:------------|:--------------------------------------|
    |1 |DEBUG      |True         |True => Display error detail on browser|
    |2 |SECRET_KEY |xxxxxx...    |It is for Django                       |
    |3 |DB_USER    |user         |It is username of your postgresql      |
    |4 |DB_PASSWORD|password     |It is password of your postgresql      |
1. Commands
    ```bash
    $ pipenv install --dev

    # Setup DB
    $ python manage.py migrate
    $ python manage.py createsuperuser
    >> ** Input information of your superuser! **

    # Run django server
    $ python manage.py runserver
    ```
1. Then, you can access to
    - `localhost:8000/admin`
    - `localhost:8000/cms`

1. You can run automated test by this command
    ```bash
    $ pipenv run test
    ```
