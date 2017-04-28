from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from apps.document.views import Document_create, Detalle_doc, \
    DocumentoCreate, DesdeCreate, ParaCreate, Document_list

urlpatterns = [
    url(r'^nuevo$', Document_create, name='document_form'),
    url(r'^nuevo/desde', DesdeCreate.as_view(), name='desde_form'),
    url(r'^nuevo/para', ParaCreate.as_view(), name='para_form'),
    url(r'^list$',Document_list.as_view(), name="documento_list"),
    url(r'^detalle/(?P<id_docum>\d+)$',Detalle_doc, name="documento_detalle"),
    ]