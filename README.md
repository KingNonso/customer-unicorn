# Customer-Unicorn

A simple CRUD app of customer data using Django Unicorn

## How to get started with this project

Please follow the following instructions to setup this project:

Clone the repo 
```
git clone https://github.com/KingNonso/customer-unicorn.git
```

## Setup/ Installation

To setup this project, you would need to enter into the cloned directory and create a virtual environment into which you
install the requirements file. And then create the sqlite3 db and migrate the database, then start the server

```
cd customer-unicorn/
virtualenv env
source env/bin/activate  # activate virtualenv for Mac OS/ Linux
env\Scripts\activate   # activate virtualenv for windows
sqlite3 db.sqlite3  # create an sqlite3 database
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # to create an admin user
python manage.py collectstatic
python manage.py runserver  # runs server at 127.0.0.1:8000 
```

Django admin server should now be accessible via [127.0.0.1/admin](http://127.0.0.1/admin)

### Project (Python/Django) + Unicorn

This project uses [Django-Unicorn](https://www.django-unicorn.com/) a magical full-stack framework for Django ✨ It
allows you to:  
* Quickly add in simple interactions to regular Django templates without learning a new templating language
* Unicorn progressively enhances a normal Django view, so the initial render of components is fast and great for SEO.
* Next, Unicorn binds to the elements you specify and automatically makes AJAX calls when needed.
* Then, Unicorn dynamically updates the DOM.

The end result is that you can focus on writing regular Django templates and Python classes without needing to switch to
another language or build unnecessary plumbing.


#### Other alternatives include

* Using REST APIS (django-rest-framework)
* Using Graphql (django-graphene)
* Using old plain Ajax 

