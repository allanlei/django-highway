from django.core.urlresolvers import get_callable

from highway.conf import settings
# from highway.signals import identified

identification_pipeline = [get_callable(identifier) for identifier in settings.HIGHWAY_IDENTICATION_PIPELINE]


def identify(**kwargs):
	route = None

	for identifier in identification_pipeline:
		try:
			route = identifier(**kwargs)
		except TypeError:
			continue

		if route:
			# identified.send(sender=identifier, **kwargs)
			return route
	return route

def identify_from_request(request, **kwargs):
	# Check if instance of request
	return identify(request=request)