from django.conf.urls import patterns, url
from views import delete, index

urlpatterns = patterns('boxer.views',
    url(r'^delete/$', delete, name="delete"),
    url(r'^$', index, name="index"),
)