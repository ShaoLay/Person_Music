from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^ranking.html/$', views.rankView, name='ranking.html'),
]