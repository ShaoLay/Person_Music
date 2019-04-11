from django.conf.urls import url, include
from .views import commentView


urlpatterns = [
    url(r'^comment/$', commentView),
]