# Technical documentation for We Predicted That pokemon battle predictor

## Step 4 - Building a web app in Django

One of the goals we decided at the start of this project was to learn a new language - Python seemed the obvious choice since the project revolved around machine learning, and it's the language of choice for many ML libraries (for example, it's the only fully supported language for tensorflow). When it came to creating a web app to interact with out model, we were keen to continue building our knowledge of Python rather than sticking with a known framework such as Rails, so we picked Django to build the app.

Django follows Model-View-Template (MVT) pattern compared to the Model-View-Controller (MVC) pattern.

The following diagram illustrates how each of the components of the MVT pattern interacts with each other to serve a user request −

![MVT](images/MVT.png)

1. Start new project pokemonweb by entering below command from command line:

```
django-admin startproject pokemonweb
```
This will create a pokemonnweb directory with following in your current directory.
- manage.py: A command-line utility that lets you interact with this Django project in various      ways.
- __init__.py: An empty file that tells Python that this directory should be                        considered a Python package.
- settings.py: Settings/configuration for this Django project. Django settings will tell     you    all about how settings work.
- urls.py: The URL declarations for this Django project; a “table of contents” of your              Django-powered site.
- wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. 

2. Create app battle :

```
python manage.py startapp battle
```
3. Run server :

```
python manage.py runserver
```
4. We decided to use PostgreSQL instead of Django default SQLite database because its a              production grade database.

5. To run tests we need to change following in settings.py:
- This setting is required so that our tests can run; even though this is not
  required when running the server locally.

```
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '']
```