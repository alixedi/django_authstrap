=============================
django_authstrap
=============================

.. image:: https://badge.fury.io/py/django_authstrap.png
    :target: http://badge.fury.io/py/django_authstrap
    
.. image:: https://travis-ci.org/alixedi/django_authstrap.png?branch=master
        :target: https://travis-ci.org/alixedi/django_authstrap

.. image:: https://pypip.in/d/django_authstrap/badge.png
        :target: https://crate.io/packages/django_authstrap?version=latest


Bootstrap templates for django.contrib.auth

Introduction
------------

Django comes with a reasonable default authorization module comprising of several useful views such as login and logout, password reset flow and password change flow. Neither the templates for these views nor the urls are part of the standard django distribution. This projects implemnts the missing functionality so you don't have to. 

Installation
------------

Install django-auth-bootstrap-templates: ::

    pip install django_authstrap

Usage
-----

Then use it in a project:

1. Put this in your settings.py: ::

	INSTALLED_APPS += 'django_authstrap'
	LOGIN_URL = 'auth/login'
	LOGOUT_URL = 'auth/logout'

2. Set-up the project urls.py to include auth urls: ::

    url(r'^auth/', include('django_authstrap.urls'))

Run the dev server and point your browser to a page that required logging in.


Features
--------

* All tempaltes are based on Bootstrap 2
* Forms are rendered using the form-horizontal layout
