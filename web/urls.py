from django.conf.urls import patterns, url
from lisa.plugins.XBotMC.web import views

urlpatterns = patterns('',
    url(r'^$',views.index),
)
