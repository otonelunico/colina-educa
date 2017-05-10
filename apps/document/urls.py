from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from apps.document.views import Document_create, Detalle_doc, Create_value, Active_off, Documento_list, Documento_edit, \
    DocumentoCreate

urlpatterns = [
    url(r'^nuevo$', Document_create, name='document_form'),
    url(r'^nuevo/(?P<value>\w+)$', Create_value, name='create_value'),
    url(r'^active_off/(?P<value>\w+)/(?P<id_value>\d+)$', Active_off, name='active_off'),
    url(r'^list/$', Documento_list, name="documento_list"),
    url(r'^detalle/(?P<id_docum>\d+)$',Detalle_doc, name="documento_detalle"),
    url(r'^editar/(?P<id_documento>\d+)$',Documento_edit, name="documento_edit"),
    ]