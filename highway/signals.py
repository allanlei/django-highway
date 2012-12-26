from django.dispatch import Signal


pre_route_change = Signal(providing_args=['from_route', 'to_route'])
route_changed = Signal(providing_args=['from_route', 'to_route'])

route_entered = Signal(providing_args=['route'])
route_exited = Signal(providing_args=['route'])