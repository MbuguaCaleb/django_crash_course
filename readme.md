**Creating a Virtual Environment**

```
Having installed pipenv globally by

pip3 install pipenv

Run

pipenv shell


(a)pipfile is created which lists all the files we install

(b)All packages are installed in the virtual enviroment as
opposed to globally

```

**Installing Django **

```

pip install django

```

**Project and Apps**

```
A project is the overview of you application.

A project can have many apps

Project Structure
(a)manage.py ->CLT Tool for django..

(b)init.py

(c)settings.py->as name suggests(i initialise all my apps, middleware etc)

(d)URLS Py..

every app has a url

Creating an App

python manage.py startapp polls


```

**Running app**

```
(a)Default 8000 PORT
python manage.py runserver

(b)Custom port
python manage.py runserver port


Default Migrations

(c)python manage.py migrate

```

**Migrations**

```

Running Migrations
python manage.py makemigrations polls'

Django vs Laravel

In djANGO from the Model i create the migrations..

Laravel is slightly different i link the models to migrations i create

Key concept...Models are always linked to Migrations

python manage.py migrate

```

**Django Shell Commands**

```
(a)python manage.py shell

(b)Imports so as to query DB

from polls.models import Question,Choice
from django.utils import timezone

(c)Getting all Questions

(d)Question.objects.all()

(e)Creating a Question Object
 q = Question(question_text='what is your favorite python framework?',pub_date=timezone.now())

(f)Saving a Question
 q.save()

(g)Querying from the created Question
 q.id
 q.pub_date
 q.question_text

(h)Query a Question by Filter

Question.objects.filter(id=1)

(i)Query a question by get

(j)Question.objects.get(pk=1)

Relationships

Question has choices

(a)q=Question.objects.get(pk=1)

(b)Creating a choice through this question instance
q.choice_set.create(choice_text="Django",votes=0)
q.choice_set.create(choice_text="Flask",votes=0)
q.choice_set.create(choice_text="Web2py",votes=0)

(c)Querying the Choices belonging to a Question

(d)Exiting Shell quit()


```

**Creating Django Admin User**

```
python manage.py createsuperuser

```

**Creating a Django App**

```
python manage.py startapp pages

```

**Notes By**

```
Mbugua Caleb

```
