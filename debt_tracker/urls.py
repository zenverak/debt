from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
        url(r'^$',views.main, name='main'),
        url(r'^debtors/$',views.debtor_list, name='debtor_list'),
        url(r'^companies/$',views.company_list, name='company_list'),
        url(r'^list/(?P<id>\d+)/$',views.debt_list, name='debt_list'),
        url(r'^list/\d+/pay/(?P<pk>\d+)$', views.debt_pay, name='debt_pay'),
        url(r'^debt_add/(?P<id>\d+)$', views.debt_add, name='debt_add'),
        url(r'^debtor_add/$', views.debtor_add, name='debtor_add'),
        url(r'accounts/login/$', login, name='login'),
        url(r'accounts/logout/$', logout, name='logout'),
        ]
