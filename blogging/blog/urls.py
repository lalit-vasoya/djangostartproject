from django.conf.urls import url
from django.urls import path
from .views import home,detail_view
urlpatterns = [
    url(r'^$',home,name="home"),
    url(r'(?P<id>\d+)/',detail_view,name="detail_view")
    #path('<int:id>',detail_view,name="detail_view")

]
