"""
WSGI config for article_summarizer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "article_summarizer.settings")

application = get_wsgi_application()

# this is the entry point for the WSGI server to serve the Django application
app = application