import os
import sys
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application


# path = '/home/kaelzubs/epredictz'

path = 'C:/Users/robot/Desktop/epredictz/epredictz'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'epredictz.settings'


application = get_wsgi_application()

# application = WhiteNoise(application, root='/home/kaelzubs/epredictz/epredictz/static')
# application.add_files('/home/kaelzubs/epredictz/epredictz/static/img/', prefix='statiic_img')

application = WhiteNoise(application, root='C:/Users/robot/Desktop/epredictz/epredictz/static')
application.add_files('C:/Users/robot/Desktop/epredictz/epredictz/static/img', prefix='static_img')