[![CircleCI Status](https://circleci.com/gh/siruku6/life_recorder.svg?style=svg)](https://app.circleci.com/pipelines/github/siruku6/life_recorder?branch=master)

# life_recorder
display activity log

# Requirement

## Middlewares

- postgresql

# Development

## How to construct development environment?
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

### With python on your OS
1. Install and setup postgresql
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
    ```
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
