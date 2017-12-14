from django.conf.urls import url
from django.contrib import admin
from chain.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^wallet$', wallet),
    url(r'^block$', block),
    url(r'^peers$', peers)
]
