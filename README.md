# Resources
* Writing custom django admin commands [link](https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/#module-django.core.management)
* Django running management commands form your code [link](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django.core.management.call_command)



# django_rest_tdd_udemy
follow up repository for udemy course about python, django, django rest framework, docker, travis CI, postgres [course](https://www.udemy.com/course/django-python-advanced/)

## VS Code

* needed extensions: ...
* resolve application import in django (it lint them but they works)
* Configuration for linting, formatting, ruler 120 characters
* Configuratio needs to be done for highlighting methods in code.
* Unittest configuration (through VS code wizard)
* Run configuration for django server
* Run configuration for django unit test - different name for root porject folder and app (select file and run)
* the same for docker container (later)


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

While running `docker-compose up` You can launch a process conneting to that in new tab for example for creating superuser
```
docker-compose run app sh -c "python manage.py createsuperuser"
```



## Set up django admin

## Setup db
### Adding postgres to docker
### Setup postgres in django

Use env variables defined in docker image. Those variables can be set on different enviroments e.g. AWS ECS, Kubernetes, or docker db
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS')
    }
}
```

### Mocking with unittests

Overwrite function and checks if it has been called with proper parameteres. For example not sending email.
`unittest.mock.patch` method can overwrite functionality in `with` block. It has additional tools like counting calls, returning true etc.
Use test method decorator to remove 1 second delay method used by sleep in unit test so the run fast. You need to add additional arg
```python
@patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        # use patch to mock ConnectionHandler to always set true (connection to db is available ervery time its called)
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
```


### Wainting for db
Docker compose - wait for postgres to fully start before start django server.


## Creating user management endpoint
Managing adding updating user and creating authentication token to user with other APIs in application. Create new app in django for user. Remove `migration` and `admin` and `models` from new app, because we will keep it in `core` application of our project.

### Creating user API unit test
Create tests. create serializer in application. Create view in `views.py`

### Creating token
Tokens for future can be stored in database??? Authentication may be sotred in user django app. 4 tests:
1. Test that token is created okay.
2. Test invalid credentials behaviour
3. Test trying to authenticate non existing user
4. Test request that doesnt provide a password

We need to create new authenthication serializer in user app.

