from django.conf.urls import include, url
from django.contrib import admin

from payment_app.views import payment_details
urlpatterns = [

    url(r'^payments/', include('payments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pay/(?P<payment_id>\d+)/$', payment_details),

]
