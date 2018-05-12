from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'register/$', views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login/$',views.login),
    url(r'^cart/$', views.cart),
    url(r'^user_info/$',views.user_info),
    url(r'^user_order/$',views.user_order),
    url(r'^user_site/$', views.user_site),
    url(r'^order/$', views.place_order),
    url(r'^list/$', views.list),
    url(r'^detail/$', views.detail),
]
