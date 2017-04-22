from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from apps.document.views import \
    DocumentoCreate, DesdeCreate, ParaCreate, Documentopdf

urlpatterns = [
    url(r'^nuevo$', DocumentoCreate.as_view(), name='document_form'),
    url(r'^nuevo/desde', DesdeCreate.as_view(), name='desde_form'),
    url(r'^nuevo/para', ParaCreate.as_view(), name='para_form'),
    url(r'^documentopdf/$',Documentopdf.as_view(), name="pdf"),
    ]