# Writing your first Django app Part 1
> [django tutorial documentation](https://docs.djangoproject.com/en/1.11/intro/)

> [django-admin documentation](https://docs.djangoproject.com/en/1.11/ref/django-admin/)

> [Datebase API reference](https://docs.djangoproject.com/en/1.11/topics/db/queries/)

> [Template guide](https://docs.djangoproject.com/en/1.11/topics/templates/)

> [Request and Response documentation](https://docs.djangoproject.com/en/1.11/ref/request-response/)

> [Avoiding race conditions using F()](https://docs.djangoproject.com/en/1.11/ref/models/expressions/#avoiding-race-conditions-using-f)

> [Generic views documentation](https://docs.djangoproject.com/en/1.11/topics/class-based-views/)

> [The static files howto](https://docs.djangoproject.com/en/1.11/howto/static-files/)

> [The staticfiles reference](https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/)

> [Deploying static files](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/)

Commands
* `python manage.py runserver`
* `python manage.py runserver 8080`
* `python manage.py startapp polls`
* `python manage.py migrate`
* `python manage.py makemigrations polls`
* `python manage.py sqlmigrate polls 0001`
* `python manage.py shell`
* `python manage.py createsuperuser`
* `python manage.py runserver`
* `python manage.py test polls`

## Creating a project
`django-admin startproject mysite`

These folders and files will be created:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

## The development server
`python manage.py runserver`

You'll see the following output on the command line:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

August 07, 2017 - 15:50:53
Django version 1.11, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Set the port
`python manage.py runserver 8080`

## Creating the Polls app
`python manage.py startapp polls`

These folders and files will be created:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Write your first view

Open th file `polls/views.py` and put the following code in it:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")
```

Create a file `polls/urls.py` for mapping the function `index` to a URL
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

Point the root URLconf at the `polls.urls` module. Add following code to `mysite/urls.py`:
```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```

The **url()** function is passed four arguments, two required: **regex** and **view**, and two optional: **kwargs**, and **name**.

# Writing your first Django app, part 2
## Database setup

Default setting in `mysite/settings.py` `DATABASES`
* **ENGINE** - Either `django.db.backends.sqlite3`, `django.db.backends.postgresql`, `django.db.backends.mysql`, or `django.db.backends.oracle`. Other backends are also available.
* **NAME** -  The name of your database. If you’re using SQLite, it should be the full absolute path of that file.

If you are not using SQLite, additional settings such as **USER**, **PASSWORD**, and **HOST** must be added. [Reference documentation](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-DATABASES)

Create database:
`python manage.py migrate`

## Creating models

We will create two models: **Question** and **Choice**.
A **Question** has a question and a publication date.
A **Choice** has two field: the text of the choice and a vote tally.
Each **Choice** is associated with a **Question**.

Edit the `polls/models.py` file:
```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## Activating models

First, you should add the app **polls** to your project.

In `mysite/settings.py`:
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Then, make migrations:

`python manage.py makemigrations polls`

You should see following:
```
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
```

The **sqlmigrate** command takes migration names and returns their SQL (just print):

`python manage.py sqlmigrate polls 0001`

Last, run **migrate**:

`python manage.py migrate`

### Three-step guide to making model changes
* Change your models(in `models.py`)
* Run `python manage.py makemigrations` to create migrations for those changes
* Run `python manage.py migrate` to apply those changes to the database

## Playing with the ORM API

Using this instead of simply typing **python**, because manage.py sets the **DJANGO_SETTINGS_MODULE** environment variable.

`python manage.py shell`

```python
>>> from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object>]>
```

**<Question: Question object>** is, utterly, an unhelpful representation of this object.
Let's fix that by editing the **Question** model in the `polls/models.py`
```python
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choic_text
```

Try other APIs:
```python
>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

## Introducing the Django Admin

### Creating an admin user
`python manage.py createsuperuser`

Enter your desired username and password.(admin/admintest)

### Start the development server and login in
`python manage.py runserver`

Admin url(default): http://127.0.0.1:8000/admin/

### Make the poll app modifiable in the admin
Open the `polls/admin.py` and edit it:
```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

### Explore the free admin functionality
* Add new **Question**
* Change existed **Question** record
* Watch the record change history

# Writing your first Django app Part 3

## Writing more views
Let's add a few more views to `polls/views.py` :
```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Wire these new views into `polls/urls.py` module by adding the following **url()** calls:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```
**?P<question_id>** defines the name that will be sended to the view function as an argument.

## Write views that actually do something

New **index()** view(`polls/views.py`) displays the latest 5 poll questions in the system, separated by commas, according to publication date:
```python
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```

### Using templates
Create a directory called **templates** in your **polls** directory. (**DjangoTemplates** looks for a "templates" subdirectory in each of the **INSTALLED_APPS**)

Create another directory called **polls** and within that create a file called **index.html** (`polls/templates/polls/index.html`)

PUt the following code in that template:
```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Now let's update our **index** view in `polls/views.py` to use the template:
```python
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

### A shortcut: render()
It's a very common idiom to load a template, fill a context and return an **HttpResponse** object. Django provides a shortcut:
```python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

## Raising a 404 error
Raising 404 in detail page, edit `polls/views.py`:
```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

New template `templates/polls/detail.html`
```html
{{ question }}
```

### A shortcut: get_object_or_404()
It's a very common idiom to use **get()** and raise **Http404** if the object doesn’t exist. Django provides a shortcut：
```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

The **get_object_or_404()** function takes a Django model as its first argument and an arbitrary number of keyword arguments,
which it passes to the **get()** function of the model’s manager.
It raises **Http404** if the object doesn’t exist.

There’s also a **get_list_or_404()** function, which works just as **get_object_or_404()** – except using **filter()** instead of **get()**. It raises **Http404** if the list is empty.

## Use the template system
Update `polls/templates/polls/detail.html`:
```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

The template system uses dot-lookup syntax to access variable attributes.
Method-calling happens in the **{% for %}** loop: **question.choice_set.all** is interpreted as the Python code **question.choice_set.all()**

## Removing hardcoded URLs in templates
In the `polls/index.html`, the lnk was partially hardcoded like this:
```html
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```
Since you defined the **name** argument in the **url()** functions in the **polls.urls** module,
you can remove a reliance on specific URL paths defined in your url configurations by using the **{% url %}** template tag:
```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

The way this works is by looking up the URL definition as specified in the `polls.urls` module.
```python
...
# the 'name' value as called by the {% url %} template tag
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
...
```

## Namespacing URL names
Add an app_name to set the app namespace:
```python
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

Now change your `polls/index.html`:
```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

# Writing your first Django app, part 4

## Write a simple form
Let's update our poll detail template `polls/detail.html`, so that it contains a **form** element:
```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

Update our **vote()** view in `polls/views.py`:
```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

* **request.POST** is a dictionary-like object that lets you access submitted data by key name.
* **request.POST['choice']** will raise KeyError if choice wsn;t provided in POST data.
* **reverse()** function helps avoid having to hardcode a URL in the view function

After somebody votes in a question, the **vote()** view redirects to the results page for the question. Let’s write that view:
```python
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

Create a `polls.results.html` template:
```html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

## Use generic views: Less code is better
We will:
* Convert the URLconf.
* Delete some of the old, unneeded views.
* Introduce new views based on Django’s generic views.

### Amend URLconf
Edit `polls/urls.py`:
```python
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```
Note that the name of the matched pattern in the regexes of the second and third patterns has changed from **question_id** to **pk**.

### Amend views
Remove our old **index**, **detail**, and **results** views and use Django’s generic views instead.
To do so, open the `polls/views.py` file and change it like so:
```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
```

**ListView** and **DetailView** abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”
* Each generic view needs to know what **model** it will be acting upon. This is provided using the **model** attribute.
* The **DetailView** generic view expects the primary key value captured from the **URL** to be called "pk", so we’ve changed **question_id** to **pk** for the generic views.
* DetailView generic view uses a template called app_name/modelname_detail.html. In our case, it would use the template "polls/question_detail.html".
* **ListView** generic view uses a template called app_name/modelname_list.html. In our case, it would use the template "polls/question_list.html".
* For **DetailView** the question variable is provided automatically – since we’re using a Django model **Question**

# Writing your first Django app, part 5

## Writing our first test

### We identify a bug
**Question.was_published_recently()** method returns **True** if the Question’s pub_date field is in the future
```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # create a Question instance with pub_date 30 days in the future
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # was it published recently?
>>> future_question.was_published_recently()
True
```

### Create a test to expose the bug
Put the following in the `polls/tests.py`:
```python
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

### Running tests
`python manage.py test polls`

You'll see something like:
```python
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

### Fixing the bug
**Question.was_published_recently()** should return **False** if its pub_date is in the future.
```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Run the test again:
```python
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

Add more tests
```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

And now we have three tests that confirm that Question.was_published_recently() returns sensible values for past, recent, and future questions.

## Test a view

### The Django test client
Django provides a test **Client** to simulate a user interacting with the code at the view level. We can use it in **tests.py** or even in the **shell**.
```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```
[setup_test_environment()](https://docs.djangoproject.com/en/1.11/topics/testing/advanced/#django.test.utils.setup_test_environment) installs a template renderer which will allow us to examine some additional attributes on responses such as response.context

Next we need to import the test client class
```python
>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
```

With that ready, we can ask the client to do some work for us:
```python
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```

### Improving our view
In `polls/views.py`, we need to amend the **get_queryset()** method and change it so that it also checks the date by comparing it with **timezone.now()**
```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
```

**Question.objects.filter(pub_date__lte=timezone.now())** returns a queryset containing **Questions** whose **pub_date** is less than or equal to **timezone.now**.

### Testing our view
Create new test class and test cases in `polls/tests.py`:
```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
```

All work fine, but users can visit the **Question** whose **pub_date** is in the future.

Add a constraint to **DetailView** in `polls/views.py`:
```python
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Then, add some tests to check that.
```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

# Writing your first Django app, part 6

## Customize your app's look and feel
First, create a directory called **static** in your `polls/`. Django will look for static files there.

Then, create static file like `polls/static/polls/style.css`, you can refer to this static file as `polls/style.css`.

Put the following code in that stylesheet (`polls/static/polls/style.css`):
```css
li a {
    color: green;
}
```

Refer to the style.css in `index.html`:
```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

The **{% static %}** template tag generates the absolute URL of static files.

## Adding a background-image
Add the background style to your stylesheet `polls/static/polls/style.css`:
```css
body {
    background: white url("images/background.gif") no-repeat right bottom;
}
```

# Writing your first Django app, part 7

## Customize the admin form
Customize how the admin form looks. Replace the **admin.site.register(Question)** line with:
```python
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```

This particular change above makes the **Publication date** come before the **Question** field:

<img src="https://docs.djangoproject.com/en/1.11/_images/admin07.png">

Split the form up into fieldsets:
```python
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```

The first element of each tuple in **fieldsets** is the title of the fieldset. Here’s what our form looks like now:

<img src="https://docs.djangoproject.com/en/1.11/_images/admin08t.png">

## Adding related objects
A **Question** has multiple **Choice**s, and the admin page doesn’t display choices.

Register Choice with the admin just as we did with Question.
```python
from django.contrib import admin
from .models import Choice, Question
# ...
admin.site.register(Choice)
```

Another method, remove the **register()** call for the **Choice** model. Then, edit the **Question** registration code to read:
```python
from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```

 It takes a lot of screen space to display all the fields for entering related Choice objects. 
 For that reason, Django offers a tabular way of displaying inline related objects; 
 You just need to change the **ChoiceInline** declaration to read:
 ```python
 class ChoiceInline(admin.TabularInline):
    #...
```

## Customize the admin change list
Use **list_display** to display a tuple of field names.
```python
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date')
```

More info about [list_display](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

Note that the column header for was_published_recently is, by default, the name of the method.

You can improve that by giving that method `in polls/models.py` a few attributes, as follows:
```python
class Question(models.Model):
    # ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```

Edit your `polls/admin.py` file again and add an improvement to the **Question** change list page: filters using the **list_filter**.
Add the following line to QuestionAdmin:
```python
list_filter = ['pub_date']
```

Let’s add some search capability:
```python
search_fields = ['question_text']
```

Other capabilities:
* [Change list pagination](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page)
* [Search Boxes](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
* [Filters](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter)
* [Data-hierarchies](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy)
* [Column-header-ordering](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

## Customize the admin look and feel

Create a templates directory in your project directory (the one that contains **manage.py**)
Open your settings file `mysite/settings.py` and add **DIRS** option in the **TEMPLATES** setting:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Create a directory called **admin** inside **templates**, and copy template `django/contrib/admin/templates/admin/base_site.html` from the default Django admin template directory into that directory.

Edit the file and replace `{{ site_header|default:_('Django administration') }}` with your own site’s name as you see fit.
You should end up with a section of code like:
```html
{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">Polls Administration</a></h1>
{% endblock %}
```

In an actual project, you would probably use the [django.contrib.admin.AdminSite.site_header](https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.AdminSite.site_header)
attribute to more easily make this particular customization.
