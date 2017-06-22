from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$',views.debtor_list, name='debtor_list'),
        url(r'^list/(?P<id>\d+)/$',views.debt_list, name='debt_list'),
        url(r'^list/\d+/pay/(?P<pk>\d+)$', views.debt_pay, name='debt_pay'),
        url(r'^debt_add/(?P<id>\d+)$', views.debt_add, name='debt_add'),
        url(r'^debtor_add/$', views.debtor_add, name='debtor_add'),
        ]
