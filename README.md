# flask-superheroes-hw

Run dev:
```
$ (sudo) docker-compose up -d --build
$ (sudo) docker-compose exec web python manage.py create_db
$ (sudo) docker-compose exec web python manage.py seed_db #fills database with test data (hardcoded in manage.py)
```
App is running on http://localhost:5000/

Run prod:
```
$ (sudo) docker-compose -f docker-compose.prod.yml up -d --build
$ (sudo) docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
$ (sudo) docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db
```
App is running on http://localhost:1337
