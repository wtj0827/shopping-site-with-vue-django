## Django Vue Shopping Site

## Installing

You need to have `virtualvenv` and Python 3 installed (Django 2 requires Python 3) then:

First create a new virtual environment and activate it with:

```bash
 pyghon -m venv venv
 venv/Scripts/activate
```
Next, clone the project from Github:

```bash
git clone https://github.com/techiediaries/django-auth0-vue
cd django-auth0-vue
```

Install the project requirements using pip:

```bash
python manage.py makemigrations
python -m pip install ...
python manage.py migrate
python manage.py runserver
```

Next install the Vue.js dependencies and run the front-end dev server with:

```bash
cd vueapp
npm install
npm run dev
```

You can now navigate with your web browser to http://localhost:8000 and start playing with the demo.
