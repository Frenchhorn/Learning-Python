# Advanced tutorial: How to write reusable apps

## Your project and your reusable app
After the previous tutorials, our project should look like this:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    polls/
        __init__.py
        admin.py
        migrations/
            __init__.py
            0001_initial.py
        models.py
        static/
            polls/
                images/
                    background.gif
                style.css
        templates/
            polls/
                detail.html
                index.html
                results.html
        tests.py
        urls.py
        views.py
    templates/
        admin/
            base_site.html
```

The **polls**s directory could now be copied into a new Django project and immediately reused.
It’s not quite ready to be published though. For that, we need to package the app to make it easy for others to install.

## Installing some prerequisites
`pip install setuptools`

## Packaging your app
- First, create a parent directory for polls, outside of your Django project. Call this directory **django-polls**.
- Move the **polls** directory into the **django-polls** directory.
- Create a file `django-polls/README.rst` with the following contents:
```rst
=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```
- Create a `django-polls/LICENSE` file. Choosing a license is beyond the scope of this tutorial, but suffice it to say that code released publicly without a license is useless.
- Next we'll create a `setup.py` file which provides details about how to build and install the app.
```python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
```
- Only Python modules and packages are included in the package by default. To include additional files, we’ll need to create a MANIFEST.in file.
```
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *
```

- It’s optional, but recommended, to include detailed documentation with your app. Create an empty directory django-polls/docs for future documentation. Add an additional line to django-polls/MANIFEST.in:
`recursive-include docs *`

- Try building your package with `python setup.py sdist` (run from inside `django-polls`). This creates a directory called dist and builds your new package, `django-polls-0.1.tar.gz`.

## Using your own package
- To install the package, use `pip install --user django-polls/dist/django-polls-0.1.tar.gz`
- With luck, your Django project should now work correctly again. Run the server again to confirm this.
- To uninstall the package, use `pip uninstall django-polls`: