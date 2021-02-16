# UCT Maths Competition

This is what the website [https://uctmaths.j5int.com/](https://uctmaths.j5int.com/) is based from. It allows teachers to sign-up their school and students for the upcoming UCT Mathematics Competition. Once that is done, the admins are able to allocate all students to venues for the competition and then record their scores and prizes afterwards.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installation and set-up

A step by step series of instructions on how to get a development env running. This project runs on Python 2.7.
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

*Note: most of the libraries are extremely out of date. Updating any of them should be done with care. Many features used in Django 1.6 were deprecated soon thereafter. We updated from 1.6 to 1.7 in January 2021, so there might still be a few bugs latent from 1.6.*

* Create a "uctmaths" database and user on postgres

* Create a file `uctMaths/uctMaths/settings.ini` based off of the example [uctMaths/uctMaths/EXAMPLE_settings.ini](uctMaths/uctMaths/EXAMPLE_settings.ini).
    * Database settings refer to your postgres database settings.
    * The secret key can be set manually but should be something difficult to crack as it is used for encryption
    * TEMPLATE_DIR should be the absolute path to `uctMaths/competition/interface` in your filesystem.
    * Mail settings can be configured with Mailhog.

* Sync database (create tables based on your Django models) and create superuser (`syncdb` is deprecated from Django 1.8, only use migrations for Django 1.7 onwards)

```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py makemigrations
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py migrate
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py syncdb
```

* Start Django server
```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py runserver
```

* For certain features, you need to open another terminal tab at the same time and run
```
(uctmaths_venv)~/work/uct-maths-competition/uctMaths$ python manage.py process_tasks
```
This handles background tasks that would be too slow for the server to handle. For example, generating all answer sheets and sending emails to all schools.

If you open [localhost:8000](http://localhost:8000) in your browser you should be able to access the website as users would see it. Open [localhost:8000/admin](http://localhost:8000/admin) to perform admin duties. You need to add yourself as a superuser in order to log in here. 

Following the steps outlined here, you will have a clean DB. You should ask one of the admins of the official website to provide a copy of the live database. When using a copy of the live database, make sure that you are not sending out emails to the teachers with registered email addresses. 

If you are given the database as a `.sql.gz` file, you should open it with an archiver utility such as WinRAR/7zip and extract the contained `.sql` file somewhere convenient. Using the terminal, navigate to the directory where the SQL file was saved. You can now import the database by running
```
psql -U postgres uctmaths < (filename).sql
```
where you can replace "postgres" with the name of the user owning the database.


## Modifying database models
The Django workflow is that changes to database models should only be done in a `model.py` file in a Django app. For example: [uctMaths/competition/model.py](uctMaths/competition/model.py). After you have changed the model, rerun `python manage.py makemigrations` and `python manage.py migrate`, and then check that the changes have been reflected in the database (use pgadmin). When you make your changes live, you will have to perform the migrations again. If you add columns manually, Django will become confused and you will have to write and run SQL scripts manually to reflect the changes. See [uctMaths/scripts/add_new_columns_022021.sql](uctMaths/scripts/add_new_columns_022021.sql) as an example of this.

Before making changes to models, check that you have an initial migration which is up-to-date with the database. If there is not an initial migration, Django will think that the next migration is the initial one, and if a table already exists, it will not make changes since the initial changes are typically for creating tables.

Check if there are migrations that need to be made every time you pull.

## Where to look
There are some good docs in [docs/userdoc](docs/userdoc) and [docs/readme](docs/readme). These were written in 2014, so are quite out of date.

[uctMaths/manage.py](uctMaths/manage.py) is the main file which you will typically run with `python manage.py runserver`.

[uctMaths/uctMaths](uctMaths/uctMaths) mainly contains configuration and settings for the server. Most of the useful files are in [uctMaths/competition](uctMaths/competition).

Some of the important files:
* [uctMaths/competition/models.py](uctMaths/competition/models.py): all of the classes which are used for turning database entities into objects in Python. The class attributes should match the columns in the database tables.
* [uctMaths/competition/admin.py](uctMaths/competition/admin.py): this is where the admin operations get defined. Each class represents the admin import-export model where you can select entries and apply actions. To add new actions (items in the drop-down menu), add a new string to the `actions` attribute, then add a method with this same name and assign it a short description to show in the drop-down.
Action buttons can be created for actions that are independent of the selected items. Add a URL for the button's method, and then add a button to the HTML file referenced in the `change_list_template` field.
* [uctMaths/competition/compadmin.py](uctMaths/competition/compadmin.py): the methods in [admin.py](uctMaths/competition/admin.py) call functions in this file. This is where the actions get performed.
* [uctMaths/competition/urls.py](uctMaths/competition/urls.py): mapping URLs to functions. If you want to add new buttons and pages, this is likely where you will do it.
* [uctMaths/competition/views.py](uctMaths/competition/views.py): the URLs map to functions here. These functions return HTML pages that have been formatted. You can replace fields in the HTML pages here to allow pages to be dynamic.
