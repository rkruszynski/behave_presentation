# behave_presentation
Django aplication and behave e2e tests for it


How to start app for the first time:
```
cd django-app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
How to run behave tests:
```cd behave-app
behave features\test_name.feature
```
