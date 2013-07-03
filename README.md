# django-txtlocal

For sending and receiving text messages (SMS) from textlocal.com


## Installation

    pip install django-txtlocal


### If you're recieving messages

Add to your `urls.py`:

    url(r'^', include('txtlocal.urls'))

Add to your `settings.py`:

    INSTALLED_APPS = (
        ...,
        'txtlocal',
        ...,
    )

Run:

    ./manage.py syncdb


### If you're sending messages

Add to your `settings.py`:

    TXTLOCAL_USERNAME = Your username with textlocal
    TXTLOCAL_PASSWORD = Your password with textlocal
    TXTLOCAL_FROM = Word up to 11 characters or number up to 14 digits. String.

You can also set `TXTLOCAL_ENDPOINT`. This defaults to 'https://www.txtlocal.com/sendsmspost.php'


## Infrequently Asked Questions

**Why txtlocal, not tExtlocal?**

Because textlocal.com used to be txtlocal.co.uk
