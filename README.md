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

## API Reference

#### Form

```http
  GET /apply/get_form
```

Renders an HTML form that takes applicant information and CV/Resume as a pdf.

#### Submit data to database

```http
  POST /apply/get_form
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email `      | `string` | **Required**.valid email |
| `firstName `      | `string` | **Required**. User name |
| `lastName `      | `string` | **Required**.valid email |
| `experience-level `      | `string` | **Required**. experience-level |
| `visa-status `      | `string` | **Required** visa-status |
| `salary-expect `      | `string` | salary-expect |
| `ph-no `      | `string` | ph-no  |
| `employment-status `      | `string` | **Required** employment-status |
| `gender `      | `string` | gender |
| `resume `      | `string` | **Required**. User name |

The API saves user in a local Postgres table. There are two tables, one that saves the resume and other that saves all the other info.
The resume table id is a foreign key in the candidate-tb so it is accessed from their.

#### Last Page

```http
  GET /apply/get_ending/
```
After the form is submitted the user is shown an ending page
where he is told to wait for the company's  response

## 🛠 Skills
Python , 
Django ,
Postgres ,
Database Design.

