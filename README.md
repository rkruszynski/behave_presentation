## Django aplication and behave e2e tests for it


### How to start app for the first time:
```
cd django-app
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
There are several features in final_feature\ If you want to run those: make sure that you have user with login 'admin' and password 'test1234'. This can be the user created with 'createsuperuser' 

### Next time just:
```
cd django-app
python manage.py runserver
```

### How to run behave tests:
(make sure that you start selenium server before)
```cd behave-app
# One feature file:
behave feature_path\feature_name
# All features in folder:
behave feature_path
```

Selenium server is attached to this project. You can run it by:
```
cd behave-app\selenium
java -jar selenium-server-standalone-2.53.1.jar
```
