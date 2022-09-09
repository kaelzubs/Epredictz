import os
import sys
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application


path = '/epredictz/epredictz'

# path = 'C:/Users/robot/Desktop/epredictz/epredictz'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'epredictz.settings'


application = get_wsgi_application()

WhiteNoise(application)

# application = WhiteNoise(application, root='C:/Users/robot/Desktop/epredictz/epredictz/static')
# application.add_files('C:/Users/robot/Desktop/epredictz/epredictz/static/img', prefix='static_img')