from django.http import Http404

def highway_not_found_handler():
	raise Http404()