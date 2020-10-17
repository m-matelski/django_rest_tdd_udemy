# django_rest_tdd_udemy
follow up repository for udemy course about python, django, django rest framework, docker, travis CI, postgres [course](https://www.udemy.com/course/django-python-advanced/)

## Convention
* `docker-compose run app sh -c "python manage.py startapp core"` - core application for keepeing all db and migrations code. (remove views and tests).
* tests folder inside app folder
* add `core` app to settings
* use `docker-compose run app sh -c "python manage.py test && flake8"` to also run flake lint checker

## Docker

```
docker-compose run app sh -c "python manage.py test"
```

good practice to impirt user model
``` python
from django.contrib.auth import get_user_model
```