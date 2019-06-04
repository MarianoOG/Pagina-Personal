from django.conf.urls import url
from . import views

app_name = "main"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^en$', views.IndexViewEN.as_view(), name='indexEN'),
    url(r'^robots.txt$', views.robots, name="robots"),
    url(r'^google3d8b31bd23ec2d59.html$', views.google, name="googleverify")
]
