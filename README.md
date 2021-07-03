[![CircleCI Status](https://circleci.com/gh/siruku6/life_recorder.svg?style=svg)](https://app.circleci.com/pipelines/github/siruku6/life_recorder?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8818b78f606cad7164c/maintainability)](https://codeclimate.com/github/siruku6/life_recorder/maintainability)

# life_recorder
Display activity log  
In the future, these logs are showed in the form of chart (perhaps...)

# 1. Requirement

You need to setup these and to enable `docker-compose` to run.

- docker
- docker-compose

## Other Middlewares

- pipenv
- postgresql

**\*You don't have to setup these Middlewares in your OS, if you build your environment with docker and docker-compose !!**

# 2. Development

## How to build development environment?

### With Docker

<details><summary>Click here to open! :D</summary><div>

1. Create OAuth 2.0 client  
    If it is necessary, please create Google client-id following this article.
    ([Google Cloud / Creating client IDs](https://cloud.google.com/endpoints/docs/frameworks/java/creating-client-ids?hl=ja#web-client))


1. Copy `.env`
    ```bash
    $ cp .env.example .env
    ```
    |No|Name       |Value Example|Note                                   |
    |:-|:----------|:------------|:--------------------------------------|
    |1 |DEBUG      |True         |True => Display error detail on browser|
    |2 |SECRET_KEY |xxxxxx...    |It is for Django                       |
    |3 |DB_USER    |user         |It is username of your postgresql      |
    |4 |DB_PASSWORD|password     |It is password of your postgresql      |
    |- |-          |-            |The below variables are optional<br>(not required)|
    |5 |SOCIAL_AUTH_GOOGLE_OAUTH2_KEY   |000000000000-....apps.googleusercontent.com|OAuth 2.0 client ID for Google|
    |6 |SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET|xxxxxx...|OAuth 2.0 client secret for Google|

1. Execute following commands
    ```bash
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

## After building environment

### Access to APP

1. You can access to
    - Django Admin  
    `localhost:8000/admin`
    - App Top  
    `localhost:8000/cms`
    - API Root  
    `localhost:8000/api/v1`

1. You can display the sample response of API  
    `localhost:8000/api/v1/records/?format=json`

### Adding pip module

If you add any pip module,  
then you have to rewrite `requirements.txt` and rerun `docker-compose build`,  
because pip modules are installed in Docker image according to `requirements.txt`.

# 3. Contribution

Before `commit` or `push`, please run following checks, and confirm all of them are successful!

1. flake8  
    ```bash
    $ docker-compose exec web flake8
    ```

1. unittest  
    ```bash
    $ docker-compose exec python manage.py test --debug-mode
    ```
