import os

import sys

sys.path.append('/apis/apis-webpage-base')
from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apis.settings.server")

application = get_wsgi_application()

