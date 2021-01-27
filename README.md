# UCT Maths Competition

This is what the website [https://uctmaths.j5int.com/](https://uctmaths.j5int.com/) is based from. It allows teachers to sign-up their school and students for the upcoming UCT Mathematics Competition. Once that is done, the admins are able to allocate all students to venues for the competition and then record their scores and prizes afterwards.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installation and set-up

A step by step series of instructions on how to get a development env running

* Clone UCT Maths repository

```
~/work$ git clone https://github.com/j5int/uct-maths-competition.git
```

* Setup your virtualenv

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

* Install requirements for uct-maths-competition (Django 1.6 and other libraries)

```
(uctmaths_venv)$ cd ~/work/uct-maths-competition
(uctmaths_venv)~/work/uct-maths-competition$ pip install -r req.txt 
```

Note: most of the libraries are extremely out of date. Updating any of them should be done with care. Many features used in Django 1.6 were deprecated soon thereafter.


* Create a "uctmaths" database and user on postgres

* Create a file `settings.ini` based off of the example `\uctMaths\uctMaths\EXAMPLE_settings.ini`

Database settings refer to your postgres database settings.
The secret key can be set manually but should be something difficult to crack as it is used for encryption
Template dir is the directory for `uctMaths\competition\interface`.
Mail settings can be configured with Mailhog.


* Sync database (create tables based on your Django models) and create superuser (deprecated in Django 1.8, use migrations for Django 1.7 onwards)

```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py syncdb
```

* Start Django server

```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py runserver
```

If you open `localhost:8000` in your browser you should be able to access the website as users would see it. Open `localhost:8000/admin` to perform admin duties. You need to add yourself as a superuser in order to use this. Following the steps outlined here, you will have a clean DB. You should ask one of the admins of the official website to provide a copy of the live database. When using a copy of the live database, make sure that you are not sending out emails to the teachers with registered email addresses. 


## Where to look

