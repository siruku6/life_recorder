[![CircleCI Status](https://circleci.com/gh/siruku6/life_recorder.svg?style=svg)](https://app.circleci.com/pipelines/github/siruku6/life_recorder?branch=master)

# life_recorder
display activity log

# Requirement

## 1. Middlewares

- postgresql

## 2. Environment Variables
Copy from .env.example to .env, then rewrite it.

```bash
$ cp ./life_recorder/.env.example ./life_recorder/.env
$ vim ./life_recorder/.env
```
|No|Name       |Value Example|Note                                   |
|:-|:----------|:------------|:--------------------------------------|
|1 |DEBUG      |True         |True => Display error detail on browser|
|2 |SECRET_KEY |xxxxxx...    |It is for Django                       |
|3 |DB_USER    |user         |It is username of your postgresql      |
|4 |DB_PASSWORD|password     |It is password of your postgresql      |


# Development

```
# Setup DB
$ python manage.py migrate
$ python manage.py createsuperuser

# Run django server
$ python manage.py runserver
```
Then, you can access `localhost:8000/cms/logs`, `localhost:8000/admin` !
