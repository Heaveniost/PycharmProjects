from django.conf.urls import url
from df_goods import views

urlpatterns = [
    # url(r'^$',views.index),
    # url(r'register/$', views.register),
    # url(r'^register_handle/$',views.register_handle),
    # url(r'^login/$',views.login),
    # url(r'^info/$',views.info),
    # url(r'^order/$',views.order),
    # url(r'^cart/$',views.order),
    url(r'^list/$', views.list),
    url(r'^detail/$', views.detail),
]
