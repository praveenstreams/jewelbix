
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jwelB.settings')

# application = get_wsgi_application()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jwelB.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
