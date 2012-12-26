from highway.conf import settings


def cookies(request=None):
	return request.COOKIES.get(settings.HIGHWAY_ROUTE_KEY)

def header(request=None):
	key = settings.HIGHWAY_ROUTE_KEY.upper().replace('-', '_')
	return request.META.get('HTTP_{key}'.format(key=key))

def querystring(request=None):
	return request.GET.get(settings.HIGHWAY_ROUTE_KEY)

# def path(request=None):
	# return request.COOKIES.get(settings.HIGHWAY_ROUTE_KEY)