# MSF Test Project

![Logo](https://github.com/TrippleA-Ashaba/msf_project/assets/102288573/4c2573ba-2bb1-4e5c-a323-b2e91f726d44)


A frontend and a Backend API

## API Documentation

1. [Postman docs](https://documenter.getpostman.com/view/21195114/2s9YJXZQjz)

2. Spectacular Documentation http://127.0.0.1:8000/api/docs/

![spectacular](https://github.com/TrippleA-Ashaba/msf_project/assets/102288573/d0996a73-5668-4d00-8311-35769d3c6765)


_Note:_ Your local server must be running to use the **spectacular** docs.

## Setup

To setup and run this project

_Note: All commands for use in bash & unix terminals_ Tested on windows only.

**Clone the project**

```bash
$ git clone https://github.com/TrippleA-Ashaba/msf_project.git
$ cd msf_project
```

**Create Virtual Environment**

```bash
$ python -m venv .venv
$ source .venv/Scripts/activate
```

**Install Dependencies**

```bash
(.venv)$ pip install -r requirements.txt
```

**Add Environment Variable**

To run this project, you will need to add the following environment variables to your .env file

Copy contents from `sample.env` file and edit accordingly

`SECRET_KEY = 'Your Secret Key'`

`DEBUG = True`

## Run Project

_Note: For running the first time, create database tables_

```bash
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py migrate
```

Then

```bash
(.venv)$ python manage.py runserver
```

Goto `http://127.0.0.1:8000/`

## Tech Stack

**Client:** Bootstrap, JavaScript, HTMX

**Server:** Django, Django Rest Framework
