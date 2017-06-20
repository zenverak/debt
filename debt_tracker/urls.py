from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.debtor_list, name='debtor_list'),
        ]
