from highway import current_route
from highway.conf import settings

import logging
logger = logging.getLogger(__name__)

class HighwayRouter(object):
    @property
    def ignored_models(self):
        return []
        # if not getattr(self, '__ignored_models', None):
        #     from django.db.models.loading import get_models, get_model, get_app
        #     from landlord.conf import settings
        #     models = set()

        #     ignored_apps = tuple(settings.LANDLORD_ROUTER_IGNORED_APPS)
        #     for app in ignored_apps:
        #         models.update(set(get_models(get_app(app))))

        #     ignored_models = settings.LANDLORD_ROUTER_IGNORED_MODELS
        #     for model in ignored_models:
        #         models.add(get_model(*model.split('.')))

        #     self.__ignored_models = tuple(models)
        #     logger.info('Ignored models: %s', self.__ignored_models)
        # return self.__ignored_models

    def db_for_read(self, model, **hints):
        if model not in self.ignored_models:
            logger.info('read from %s: %s %s', current_route, model, hints)
            return str(current_route)
        return None

    def db_for_write(self, model, **hints):
        if model not in self.ignored_models:
            logger.info('write to %s: %s %s', current_route, model, hints)
            return str(current_route)
        return None

    def allow_syncdb(self, db, model):
        if db in []:
            return True

        if model not in self.ignored_models:
            logger.info('syncdb to %s: %s %s', current_route, db, model)
            return str(current_route)
        return None