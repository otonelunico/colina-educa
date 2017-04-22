from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.home.views import index

urlpatterns = [
    url(r'^$', login_required(index), name='home_index'),
]