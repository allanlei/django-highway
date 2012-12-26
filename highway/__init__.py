from werkzeug.local import Local, LocalProxy, LocalManager, LocalStack

from signals import pre_route_change, route_changed, route_entered, route_exited
from conf import settings


class HighwayLocal(Local):
    def __init__(self, *args, **kwargs):
        super(HighwayLocal, self).__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        was_on_route = hasattr(self, settings.HIGHWAY_ROUTE_KEY)
        previous_route = getattr(self, settings.HIGHWAY_ROUTE_KEY, None)

        super(HighwayLocal, self).__setattr__(name, value)


        route_entered.send(sender=self, route=value)

        if was_on_route and previous_route != value:
            route_changed.send(sender=self, from_route=previous_route, to_route=value)

    # def __getattr__(self, name):
        # super(HighwayLocal, self).__getattr__(name)
        # print 'getattr', name

    def __delattr__(self, name):
        super(HighwayLocal, self).__delattr__(name)
        print 'Should prevent delattr'
        # print 'delattr', name
        # Send

    def __release_local__(self):
        was_on_route = hasattr(self, settings.HIGHWAY_ROUTE_KEY)
        previous_route = getattr(self, settings.HIGHWAY_ROUTE_KEY, None)
        super(HighwayLocal, self).__release_local__()
        # print 'cleanup'
        
        if was_on_route:
            route_exited.send(sender=self, route=previous_route)



local = HighwayLocal()
routes = LocalStack()
local_manager = LocalManager([local, routes])

def get_current_route():
    # If using LocalStack
    # top = routes.top
    # return top
    return getattr(local, settings.HIGHWAY_ROUTE_KEY, None)

current_route = LocalProxy(get_current_route)