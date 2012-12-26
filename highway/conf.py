from appconf import AppConf
from django.conf import settings


class HighwayAppConf(AppConf):
	ROUTE_KEY = 'highway'
	
	IDENTICATION_PIPELINE = (
		# 'identifiers.request.cookies',
		# 'identifiers.request.header',
		# 'identifiers.request.querystring',
		# 'identifiers.reques.path',
		# 'identifiers.env',
	)

	NOT_FOUND_HANDLER = 'highway.handlers.highway_not_found_handler'