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

---
### A. With Docker

<details><summary>Click here to open! :D</summary><div>

1. Execute following commands
    ```bash
    $ cp .env.example .env
    $ docker-compose build
    $ docker-compose up -d
    $ docker attach life_recorder_web_1
    $ docker-compose exec web python manage.py createsuperuser
    >> ** Input information of your superuser! **
    ```

1. You can run automated test by this command
    ```bash
    $ docker-compose exec web python manage.py test --debug-mode

    # I recommend following options!
    $ docker-compose exec web python manage.py test --debug-mode -v 2 --pdb --keepdb
    ```
</div></details>

### B. With python on your OS

<details><summary>Click here to open! :D</summary><div>

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
1. Prepare `config/settings/localhost.py`
Copy from `localhost.sample.py` to `localhost.py`.
    ```bash
    $ cp config/settings/localhost.sample.py config/settings/localhost.py
    ```
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

1. You can run automated test by this command
    ```bash
    $ pipenv run test
    ```
</div></details>

---

## After 'A.' or 'B.'

1. You can access to
    - Django Admin  
    `localhost:8000/admin`
    - App Top  
    `localhost:8000/cms`
    - API Root  
    `localhost:8000/api/v1`

1. You can display the sample response of API  
    `localhost:8000/api/v1/records/?format=json`
