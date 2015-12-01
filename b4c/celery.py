from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

"""
To test if bitcoinrpc respond correctly use:
curl --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getinfo","params":[]}' -H 'content-type:text/plain;' http://opssbex:sbex42@127.0.0.1:18332

To run celery:
define a currency pointing to your local rpc daemon address (e.g for testnet: http://opssbex:sbex42@127.0.0.1:18332)

Using django
./manage.py runserver
./manage.py celeryd -E  -l info
./manage.py celery beat
./manage.py celerycam
"""

# USEFUL DOC : http://www.caktusgroup.com/blog/2014/06/23/scheduling-tasks-celery/

#from cc import tasks

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'b4c.settings')

#app = Celery('sbextrader', broker='amqp://guest@localhost//')
app = Celery('b4c')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))