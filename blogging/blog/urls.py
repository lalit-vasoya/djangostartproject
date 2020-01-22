from django.conf.urls import url
from django.urls import path
from .views import (home,detail_view,create_view,update_view,delete_view)

app_name="blog"
urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'^(?P<id>\d+)/$',detail_view,name="detail_view"),
    url(r'^createpost/',create_view,name="create_view"),
    url(r'^(?P<id>\d+)/updateview$',update_view,name="update_view"),
    url(r'^(?P<id>\d+)/deletepost$',delete_view,name="delete_view")
    #path('<int:id>',detail_view,name="detail_view")

]
