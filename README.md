# BoardgameStats

Some web frontend to display personal boardgame stats.


## Development

### Start Development

The next steps will create a database file:

1. Initialize models to database: `python manage.py makemigrations bgs --settings=backend.settings.development`
2. Add models and create database `python manage.py migrate --settings=backend.settings.development` 

Try recreating databases on error by deleting existing database and rerun the commands above


To run `backend` for development use
```python manage.py runserver --settings=backend.settings.development```

Some settings are private. Thus create an `.env` file in the project root directory with private settings. Required private settings are:

* SECRET_KEY

You can use this command to create a random secret key:
```python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"```


# API

## Boardgames 

`GET`

```sh
curl http://0.0.0.0:8000/bgs

```
