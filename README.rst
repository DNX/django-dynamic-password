=============================================================================
django-dynamic-password: dynamic password authentication for your web service
=============================================================================

Introduction
============

django-dynamic-password is a django application which allow you to add
dynamic password authentication for your web service.

How it works?
=============
Verifies provided password according to DYNAMIC_PASSWORD_PATTERN in your
``settings.py``. You can also enable this feature only for STAFF users, see below.

To do: explain in more details how it works.


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

Once the dynamic_password is in your Python path, you need to modify the INSTALLED_APPS setting to include the dynamic_password module:

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

    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD><yyyy>'

change it's value according to your needs.
Some examples:
    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<mm><PASSWORD><dd>'
    DYNAMIC_PASSWORD_PATTERN = '<dd><PASSWORD><yy>'

Optional: set DYNAMIC_PASSWORD_ONLY_STAFF
----------------------------------------------------

In order to enable dynamic_password only for staff users you can add this
line to your settings.py:

    DYNAMIC_PASSWORD_ONLY_STAFF = True