from django.conf import settings as djsettings
from django.core.management import call_command
from conf import settings

if len(settings.HIGHWAY_IDENTICATION_PIPELINE) == 0:
	raise Exception('Identification Pipeline is not setup.')



from signals import route_entered, route_exited
from django.dispatch import receiver

@receiver(route_entered)
def add_db(sender, route, **kwargs):
	print 'add_db', route, kwargs
	# Not a good way to do it
	djsettings.DATABASES[route] = djsettings.DATABASES['default'].copy()
	djsettings.DATABASES[route].update({
		'NAME': '{route}.db'.format(route=route),
	})

	# call_command('syncdb', database=route, interactive=False)

@receiver(route_exited)
def remove_db(sender, route, **kwargs):
	print djsettings.DATABASES
	print 'remove_db', route, kwargs