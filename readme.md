# PMT

## Pre-requisites
1. Python installed
2. Pip installed
3. Virtual environment already created

## How to run
1.  Run `pip install -r requirements.txt`

    a. This will install the libraries inside the requirements.txt

2.  Run `python manage.py migrate`

    a. This will install all the initial django tables   

3.  Run `python manage.py migrate --run-syncdb`

    a. Just to make sure all the tables are created

4. Run `python manage.py runserver`

   a. This will run the app on http://127.0.0.1:8000/

## Features

- Creating tweets
- Viewing tweets
