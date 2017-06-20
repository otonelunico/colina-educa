from django.conf.urls import url
from django.contrib.auth.decorators import login_required


from apps.cambios.views import CambiosView

urlpatterns = [
    url(r'^$', login_required(CambiosView), name='index'),
    ]