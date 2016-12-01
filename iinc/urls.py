
from django.conf.urls import url
from django.contrib import admin
from storage.views import Index_view, view, login, register, re_order
from storage.views import orders_report#, check
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
url(r'^$', Index_view.as_view(), name='start'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', login, {'template_name': 'login.html'}, name='login'),
    #url(r'^login$', login.as_view(), name='login'),
    url(r'^exit$', logout_then_login, name='logout'),
# registro de usuarios
    url(r'register$', register.as_view(), name='register'),
    url(r'morder$', re_order.as_view(), name='mkorder'),
# reports
    url(r'orders$', orders_report.as_view(), name='report_orders'),
# check in
    # url(r'check$', check.as_view(), name='check'),

]
