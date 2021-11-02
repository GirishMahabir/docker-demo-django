# Starting Docker ENV

```bash
docker-compose run django django-admin startproject core .

docker-compose up

docker container exec -it django bash
```
To move from sqlite to mysql:
```bash
docker-compose run django python manage.py migrate
python manage.py migrate
```

## Creating an app inside the project.
```bash
# Creating a student app.
docker-compose run django python manage.py startapp students
```

Create your app, Then we create migration:
```bash
docker-compose run django python manage.py makemigrations
# Check migrations/0001_initial.py
# if all good, then run:

docker-compose run django python manage.py migrate # this will create tables

MYSQL> DESCRIBE <table_name>
```

Running the server:
```bash
docker-compose run django python manage.py runserver
```

