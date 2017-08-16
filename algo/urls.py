from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
#from recursos import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [#cambiar url logout


    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),




]
