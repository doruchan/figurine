from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from scambio.models import Figurina

#urlpatterns for figurine
urlpatterns = patterns('',
	url(r'^$', "scambio.views.index"),	
    url(r'^(?P<pk>\d+)/$', 
		DetailView.as_view(
			model = Figurina,
			template_name = "scambio/detail.html")),
)
