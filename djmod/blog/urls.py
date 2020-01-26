from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import AboutusTemplateView,ContactusView
urlpatterns = [
    url(r"^aboutus/$",AboutusTemplateView.as_view() , name="aboutus"),
    url(r'^contactus/$',ContactusView.as_view(template_name="contactus.html"),name="contactus")
]
