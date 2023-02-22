- Serializer defines what data in the model we want to work with
- Serializer are connected to our ListCreateAPIView through serializer_class
- we use that to collect the data from the database (queryset) and convert to a format the frontend will understand (serialize_class)

- The entry point to the API is in core.urls (/api/)
- It is extended in our app_api to give us the ability to access a single or all posts (default)

## Using Django REST Generic Views

### [Concrete View Classes](https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)

## General setup 
### Create django project as core

### start app
add to installed apps
### start app_api
add to installed apps

### urls.py
create in app & app_api
#### core
1. include app and app_api in urlpatterns
#### app
- add index as [TemplateView]()


## Permissions
3 places where we can apply:
- Project wide
in core.settings
- Within view
- Per object

## Testing
### setup
1. Run coverage html to id where we need tests
2. In app.tests, import:
- User model (`from django.contrib.auth.models import User`)
- All other DB models (`from app.models import Post, Category`)
