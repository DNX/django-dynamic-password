=============================================================================
django-dynamic-password: dynamic password authentication for your web service
=============================================================================

**Attention!** Only for really paranoid people as me.

The project code and bugtracker is hosted on
`Bitbucket <https://bitbucket.org/DNX/django-dynamic-password/>`_ and `Github <https://github.com/DNX/django-dynamic-password/>`_.


Introduction
============

django-dynamic-password is a django application which allow you to add
dynamic password authentication for your web service.

How it works?
=============
Verifies provided password according to DYNAMIC_PASSWORD_PATTERN in your
``settings.py``. You can also enable this feature only for STAFF users, see below.

You can format the value of your DYNAMIC_PASSWORD_PATTERN according to:
http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior

**Some examples.** Let's assume that today is **September 29th, 2022**, 8:01 (09-29-2022 8:01). Say your username is "admin" and password "s3kr3t", according to your DYNAMIC_PASSWORD_PATTERN in settings.py you will have:

Case 1::

    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD>%d'
    only today valid password: s3kr3t29

Case 2::

    DYNAMIC_PASSWORD_PATTERN = '%d<PASSWORD>%H'
    only this hour valid password: 29s3kr3t08

Case 3::

    DYNAMIC_PASSWORD_PATTERN = '%d<PASSWORD>%H-%M'
    only this minute valid password: 29s3kr3t08-01

Installation
============

There are a few different ways to install dynamic_password:

Using pip
---------
If you have pip install available on your system, just type::

    pip install django-dynamic-password

If you've already got an old version of dynamic_password, and want to upgrade,
use::

    pip install -U django-dynamic-password

Installing from a directory
---------------------------
If you've obtained a copy of dynamic_password using either Mercurial or a
downloadable archive, you'll need to install the copy you have system-wide.
Try running::

    python setup.py develop

If that fails, you don't have ``setuptools`` or an equivalent installed;
either install them, or run::

    python setup.py install

How to configure dynamic_password?
==================================

If you have already installed dynamic_password app, you must proceed with the
configuration of your project.

Add dynamic_password to the INSTALLED_APPS
--------------------------------------------

Once the dynamic_password is in your Python path, you need to modify the INSTALLED_APPS setting to include the dynamic_password module::

    INSTALLED_APPS = (
        # ...,
        # Third-party
        'dynamic_password',
        # ...,
        )

Enable the custom authentication backend
-----------------------------------------

To activate this backend you need at least put dynamic_password.backends.
DynamicPasswordBackend line to the AUTHENTICATION_BACKENDS tuple:

    AUTHENTICATION_BACKENDS = (
                'dynamic_password.backends.DynamicPasswordBackend',
                )

Set the DYNAMIC_PASSWORD_PATTERN in your settings.py
----------------------------------------------------

Add this line to your settings.py:

    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD>%m'

change it's value according to your needs.
Some examples::

    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD>%d'
    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD>%m'
    DYNAMIC_PASSWORD_PATTERN = '%m<PASSWORD>%d'
    DYNAMIC_PASSWORD_PATTERN = '%d<PASSWORD>%Y'

You can format this value according to: http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior

Optional: set DYNAMIC_PASSWORD_ONLY_STAFF
----------------------------------------------------

In order to enable dynamic_password only for staff users you can add this
line to your settings.py:

    DYNAMIC_PASSWORD_ONLY_STAFF = True

Future development plans
========================
- Enable "per user" dynamic password, DYNAMIC_PASSWORD_USERS = ('user1', 'user2', )
