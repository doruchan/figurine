from django.shortcuts import render_to_response
from django.template import RequestContext
from scambio.models import Figurina, Persona, Scambio

def index(request):
	figu_list = Figurina.objects.all()
	persona_list = Persona.objects.order_by("nome")
	return render_to_response('scambio/index.html', {'figurine': figu_list, 'persone':persona_list}, context_instance=RequestContext(request))
