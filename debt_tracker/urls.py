from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.debtor_list, name='debtor_list'),
		url(r'^list/(?P<id>\d+)/$',views.debt_list, name='debt_list'),
        ]
