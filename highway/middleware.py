from django.core.urlresolvers import get_callable

from conf import settings
from highway import local, local_manager, current_route
from highway.utils import identify_from_request

import logging
logger = logging.getLogger(__name__)


class HighwayMiddleware(object):
	def __init__(self, *args, **kwargs):
		super(HighwayMiddleware, self).__init__(*args, **kwargs)
		self.highway_not_found_handler = get_callable(settings.HIGHWAY_NOT_FOUND_HANDLER)

	def process_request(self, request):
		highway = identify_from_request(request)

		if highway:
			setattr(local, settings.HIGHWAY_ROUTE_KEY, highway)
			setattr(request, settings.HIGHWAY_ROUTE_KEY, highway)
			logger.info('request: %s', current_route)
		else:
			return self.highway_not_found_handler()
		return None

	def process_response(self, request, response):
		if hasattr(request, settings.HIGHWAY_ROUTE_KEY):
			delattr(request, settings.HIGHWAY_ROUTE_KEY)

		logger.info('response: %s', current_route)
		local_manager.cleanup()
		return response