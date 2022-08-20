# APPLICANT TRACKING SYSTEM.

## Introduction

Organizations can use this application to collect RESUME/CV's and save 
applicants information like Salary, Experience, Visa Status etc in
a Postgres database.

Later the database can be queried using a frontend UI or simply
API's(SQL) to select specific candidates for jobs.

A Automatic Ranking System that ranks the candidates based on the
phrases and keywords in their CV's will be implemented in this app.










## Demo

This is the pure html form that gets served when the /apply API is called.

![image](https://user-images.githubusercontent.com/63000127/185745137-d2680760-7bb8-4768-b5df-cb3dd571e663.png)









[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Run Locally

You need python and Django installed to edit the and run the code.

Clone the project

```bash
  git clone https://github.com/HatimZ/Applicant-Tracking-System.git
```

Go to the project directory

```bash
  cd /Applicant-Tracking-System
```

### Database Management

Install Postgres Database and Open PgAdmin. Create a new local webserver 
and create a table inside the server.

Use the following names and passwords. This snippet is from the project/settings.py file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'candidate_db', # database name 
        'USER': 'postgres',     # user-name fixed
        'PASSWORD': 'pass123',  # password for Server, fixed
        'HOST': 'localhost',    # fixed
        'PORT': '5432',         # port for server fixed
    }
}
```
After creating the database server and the table.
Run the below python commands, at the level of folder where
manage.py is living.


Migrate Models to SQL commands
```python
  python manage.py makemigrations
```

Apply those SQL commands
```python
  python manage.py migrate
```

Run the local server 
```python
  python manage.py runserver
```
