from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^ecoeats/', include('ecoeats.urls')),
]
