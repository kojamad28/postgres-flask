# Postgres Flask

This repository provides a Flask project template connected with PostgreSQL database.


## Usage

Clone this repository and build a docker image.

```bash
docker compose build
```


Then initialize the database.

```bash
docker compose run flask flask --app app init-db
```
