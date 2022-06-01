
<center><img src="cohort_007.jpg"  alt="Clarusway" width="600"/></center>
<br>

<center><h1> Django Class Notes</h1></center>
<p>Clarusway<img align="right"
  src="https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg"  width="15px"></p>
<br>


# Flight Project 1 - Er diagram, Swagger, Debug Toolbar

### Nice to have VSCode Extentions:
- Djaneiro - Django Snippets

### Needs
- Python, add the path environment variable
- pip
- virtualenv
- .gitignore file
- .env file

## Summary
- Project Introduction
  - Slides
  - Difference between BRD and SRS
  - Business Requirements Document (BRD)
  - Entity Relationship (ER) Diagram
- Create project
- Secure your project
  - .gitignore
  - decouple
  - .env
- Publish your project to Github
  - Using VSCode
  - Using git commands
- PostgreSQL setup
- Django Rest Framework setup
- Install Swagger
- Install Debug Toolbar
- Seperate Dev and Prod Settings
  - First Solution: Keeping local settings in "settings_local.py"
  - Second Solution: Separate settings file for each environment
  - Django Settings: Best practices

## Project Introduction

- Explain project from slides on LMS [link](https://lms.clarusway.com/mod/page/view.php?id=15444)

### Difference between BRD and SRS

- The role of formulating a document is to understand fundamentals that will be compelled to develop robust software. Type of record expectation depends upon business type, their criteria, how company processes, and what kind of software is to be developed.

#### Business Requirement Document (BRD)

- This document serves to find out practical requirements which may occur while developing any software. It elaborates on the interest of user requirements and developer requirements.

- Following are some features of BRD:

  - It is one of few documents created in any software development life-cycle.
  - Documents features a company can provide a workable solution.
  - It is used to find out what is expected from the system.
  - It helps in finding out project sponsors.

- Example: Consider software for tracking Employees spend time. This document will picturize how a system can be made which can improve efficiency of tracking an employee.

#### Software Requirement Specification (SRS):

- This document serves as a detailed illustration of functional and non-functional requirements needed that the software should fulfill.

- Following are some features of SRS:

  - This document bridges gap between user and the developer.
  - Documents board imaginations into a structural layout.
  - Used for measuring initial costs and efforts.
  - Works as an agreement between communicating parties.

- Example: Consider a software to monitor employee performance. This will require basic modules such as Login Module, Administrator Module, Employee Module, and Reporting Module. SRS document helps to manage these modules.

#### Difference between BRD and SRS:

- BRD is maintained by Business Analyst.   SRS is maintained by Business Analyst or System Analyst.
- BRD focuses on Business requirements and Stakeholders requirements. SRS focuses on functional and non-functional requirements.
- BRD bridges the gap for understanding company features to the customer. SRS bridges the gap occurs between user and developer.
- BRD used in initiation phase.   SRS used for the planning phase.
- BRD features about why the requirements are being taken. SRS features about what requirements are being taken.
- BRD is used by Upper/middle Management teams. SRS is used by the Project managers, technical leads, and Subject matter experts.

- Explain Business Requirements Document - [BRD](https://drive.google.com/file/d/1p2bZ_2CHN2SdOoV5jDaw_4pAaNsPCJrg/view)

- Explain Entity Relationship (ER) Diagram and create the diagram on [DrawSQL](https://drawsql.app/)

- Show a sample finished ER Diagram for the project: 

![](FlightReservationERD.png)

## Create project

- Create a working directory, name it as you wish, cd to new directory.

- Create virtual environment as a best practice:
```py
python3 -m venv env # for Windows or
python -m venv env # for Windows
virtualenv env # for Mac/Linux or;
virtualenv env -p python3 # for Mac/Linux
```

- Activate scripts:
```bash
.\env\Scripts\activate  # for Windows
source env/bin/activate  # for MAC/Linux
```

- See the (env) sign before your command prompt.

- Install django:
```bash
pip install django
```

- See installed packages:
```sh
pip freeze

# you will see:
asgiref==3.3.4
Django==3.2.4
pytz==2021.1
sqlparse==0.4.1

# If you see lots of things here, that means there is a problem with your virtual env activation. 
# Activate scripts again
```

- Create requirements.txt same level with working directory, send your installed packages to this file, requirements file must be up to date:
```py
pip freeze > requirements.txt
```

- Create project:
```py
django-admin startproject main . 
# With . it creates a single project folder.
# Avoiding nested folders
```

- Various files has been created!

- Check your project if it's installed correctly:
```py
python3 manage.py runserver  # or,
python manage.py runserver  # or,
py -m manage.py runserver
```

## Secure your project

### .gitignore

- Add standard .gitignore file to the project root directory. 

- Do that before adding your files to staging area, else you will need extra work to unstage files to be able to ignore them.

### python-decouple

- To use python decouple in this project, first install it:
```py
pip install python-decouple
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- For more information look at [python-decouple documentation](https://pypi.org/project/python-decouple/)

- Import the config object on settings.py file:
```py
from decouple import config
```

- Create .env file on root directory. We will collect our variables in this file.
```py
SECRET_KEY=t5o9...
```

- You can use [django secret key generator apps](https://djecrety.ir/)

- Retrieve the configuration parameters in settings.py:
```py
SECRET_KEY = config('SECRET_KEY')
```

- From now on you can send you project to the github, but double check that you added a .gitignore file which has .env on it.

## Publish your project to Github

- The easiest way to publish your local project to github is using the VSCode extention. 

  - Open Source Control page and click "Publish to Github". 

  - Write a descriptive name and publish.

  - Push your code, set main as upstream (remote) branch name.

  - If you want, go to your Github page and change visibility or your project to "Public".

- Create a remote repo in your Github account first and follow descriptions on the page. 

## PostgreSQL setup

- To get Python working with Postgres, you will need to install the “psycopg2” module.
```py
pip install psycopg2
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

## Django Rest Framework (DRF) setup

- Get the latest installation [DRF link](https://www.django-rest-framework.org/#installation)

- Install DRF:
```py
pip install djangorestframework
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- Add 'rest_framework' to your INSTALLED_APPS setting.
```py
INSTALLED_APPS = [
    # ...
    # Third party apps:
    'rest_framework',
]
```

## Install Swagger

- Explain a [sample API reference documentation](https://shopify.dev/api)

- Swagger is an open source project launched by a startup in 2010. The goal is to implement a framework that will allow developers to document and design APIs, while maintaining synchronization with the code.

- Developing an API requires orderly and understandable documentation.

- To document and design APIs with Django rest framework we will use drf-yasg which generate real Swagger/Open-API 2.0 specifications from a Django Rest Framework API. You can find the documentation [here](https://drf-yasg.readthedocs.io/en/stable/readme.html).

- Installation:
```py
pip install drf-yasg
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- Add 'drf_yasg' to your INSTALLED_APPS setting.
```py
INSTALLED_APPS = [
   # ...
   'django.contrib.staticfiles',  
   # required for serving swagger ui's css/js files

   # Third party apps:
   'drf_yasg',
   # ...
]
```

- Here is the updated urls.py for swagger. In swagger documentation, those patterns are not up-to-date. Modify urls.py:
```py
from django.contrib import admin
from django.urls import path

# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API",
        terms_of_service="#",
        contact=openapi.Contact(email="rafe@clarusway.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Four url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
```

- Migrate:
```bash
python3 manage.py migrate  # or;
python manage.py migrate  # or;
py manage.py migrate
```

- Go to [swagger page](http://localhost:8000/swagger/) and [redoc page](http://localhost:8000/redoc/) of your project!


## Install Debug Toolbar

- The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

- See the Django Debug Toolbar [documentation page](https://django-debug-toolbar.readthedocs.io/en/latest/).

- Install the package:
```py
pip install django-debug-toolbar
```

- Update requirements.txt:
```py
pip freeze > requirements.txt
```

- Add "debug_toolbar" to your INSTALLED_APPS setting:
```py
INSTALLED_APPS = [
    # Third party apps:
    # ...
    "debug_toolbar",
    # ...
]
```

- Add django-debug-toolbar’s URLs to your project’s URLconf:
```py
from django.urls import include

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

- Add the middleware to the top:
```py
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```

- Add configuration of internal IPs to "settings.py":
```py
INTERNAL_IPS = [
    "127.0.0.1",
]
```

## Seperate Dev and Prod Settings

- When we start to deploy our Django application to the server or develop a Django application with the team, settings will be a serious problem.

- There is no built-in universal way to configure Django settings without hardcoding them. But books, open-source and work projects provide a lot of recommendations and approaches on how to do it best. Let’s take a brief look at the most popular ones to examine their weaknesses and strengths.

### First Solution: Keeping local settings in "settings_local.py"

- This is the oldest method. I used it when I was configuring a Django project on a production server for the first time. I saw a lot of people use it back in the day, and I still see it now. The basic idea of this method is to extend all environment-specific settings in the settings_local.py file, which is ignored by VCS.

  - Pros: Secrets not in VCS.
  - Cons: settings_local.py is not in VCS, so you can lose some of your Django environment settings. The Django settings file is a Python code, so settings_local.py can have some non-obvious logic. You need to have settings_local.example (in VCS) to share the default configurations for developers.

### Second Solution: Separate settings file for each environment

- This is an extension of the previous approach. It allows you to keep all configurations in VCS and to share default settings between developers.

- In this case, you make a settings package with the following file structure:

![](seperateSettings.png)

- We prefer the second solution.

- In the "main" directory, create a new folder named "settings".

- Inside "settings" folder, create;

  -  ```__init__.py``` which is the required file to create a python module.

  - ```base.py``` which will include common settings.

  - ```dev.py``` which will include developmend specific settings.

  - ```prod.py``` which will include production specific settings.

- Copy all the staff inside ```settings.py``` to ```base.py```. And delete ```settings.py```.

- ```base.py``` will be:
```py
"""
Django settings for main project.
Generated by 'django-admin startproject' using Django 4.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "rest_framework",
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

```
- ```dev.py``` will be:
```py
from .base import *


THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

```
- ```prod.py``` will be:
```py
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

```
- ```__init__.py``` will be:
```py
from .base import *


env_name = config("ENV_NAME")

if env_name == "prod":

    from .prod import *

elif env_name == "dev":

    from .dev import *

```
- Modify ```.env``` file with environment name, postgres and debug variables:
```py
ENV_NAME=dev

DEBUG=True

SQL_DATABASE=fradb

SQL_USER=postgres

SQL_PASSWORD=postgres

SQL_HOST=localhost

SQL_PORT=5432
```
- Migrate the latest changes:
```bash
python3 manage.py migrate  # or;
python manage.py migrate  # or;
py manage.py migrate
```


### Django Settings: Best practices

- Keep settings in environment variables.
- Write default values for production configuration (excluding secret keys and tokens).
- Don’t hardcode sensitive settings, and don’t put them in VCS.
- Split settings into groups: Django, third-party, project.
- Follow naming conventions for custom (project) settings.

#### This is the end of initial setup. Send this setup to your Github repo. You can use it in your projects.

## Next Steps

- In Flight App project, you will use:
  - dj-rest-auth for authentication
    - login
    - logout
    - password change
    - password reset
  - write register api
  - create flight app
    - models (flight, passenger, reservation)
    - serializers (using ModelSerializer)
      - customizations, nested serializers
    - views (using ModelViewSet)
    - urls (using router)

<br>

**<p align="center">&#9786; Happy Coding! &#9997;</p>**

<p>Clarusway<img align="right"
  src="https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg"  width="15px"></p>
