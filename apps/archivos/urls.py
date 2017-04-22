from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.archivos.views import index

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
]