from django.conf.urls import url, include

from index import views


urlpatterns = [
    url(r'^$', views.indexView, name='index'),
]