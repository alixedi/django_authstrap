========
Usage
========

To use django_authstrap in a project::

1. Put this in your settings.py: ::

	INSTALLED_APPS += 'django_authstrap'
	LOGIN_URL = 'auth/login'
	LOGOUT_URL = 'auth/logout'

2. Set-up the project urls.py to include auth urls: ::

    url(r'^auth/', include('django_authstrap.urls'))


Run the dev server and point your browser to a page that required logging in.
