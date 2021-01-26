# UCT Maths Competition

Online system for administering schools and students entering the annual UCT Mathematics Competition

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installing

A step by step series of instructions on how to get a development env running

Clone UCT Maths repository

```
~/work$ git clone https://github.com/j5int/uct-maths-competition.git
```

Setup your virtualenv

Linux:
```
~/work$ sudo pip install virtualenv
~/work$ mkdir venv
~/work$ cd work/venv
~/work/venv$ virtualenv uctmaths_venv
~/work/venv$ cd work/venv/uctmaths_venv
~/work/venv/uctmaths_venv$ source bin/activate
```

Windows:
```
~/work$ pip install virtualenv
~/work$ mkdir venv
~/work$ cd work/venv
~/work/venv$ virtualenv uctmaths_venv
~/work/venv$ cd work/venv/uctmaths_venv
~/work/venv/uctmaths_venv$ Scripts/activate
```

Install requirements for uct-maths-competition (Django 1.6 and other libraries)

```
(uctmaths_venv)$ cd ~/work/uct-maths-competition
(uctmaths_venv)~/work/uct-maths-competition$ pip install -r req.txt 
```


Create uctmaths database and user on postgres

Update settings.ini using example in \uctMaths\uctMaths\EXAMPLE_settings.ini

Database settings refer to your postgres database settings.
The secret key can be set manually but should be something difficult to crack as it is used for encryption
Template dir is the directory for uctMaths\competition\interface
Mail settings can be configured with Mailhog


Sync database (create tables based on your Django models) and create superuser

```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py syncdb
```

Start Django server

```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py runserver
```




