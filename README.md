# phone-catalog

## Getting Started
1. Clone this repository to your local machine:
```
git clone https://github.com/shahriar-fattahi/phone-catalog.git
```
2- SetUp a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
or(for Windows)
```
python -m venv venv
venv/scripts/activate
```
3- install Dependencies
```
pip install -r requirements/local.txt
```
4- make migrations
```
python manage.py makemigrations
```
5- migrate
```
python manage.py migrate
```

6- create an admin
```
python manage.py createsuperuser
```

6- run the project
```
python manage.py runserver
```