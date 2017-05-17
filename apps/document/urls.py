from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


from apps.document.views import Document_create, Detalle_doc, Create_value, Active_off, Documento_list, Documento_edit, Edit_value, \
    DocumentoCreate

urlpatterns = [
    url(r'^$', login_required(Document_create), name='document_form'),
    url(r'^nuevo$', login_required(Document_create), name='document_form'),
    url(r'^nuevo/(?P<value>\w+)$', login_required(Create_value), name='create_value'),
    url(r'^editar/(?P<value>\w+)/(?P<id_value>\d+)$', login_required(Edit_value), name='edit_value'),
    url(r'^active_off/(?P<value>\w+)/(?P<id_value>\d+)$', login_required(Active_off), name='active_off'),
    url(r'^list/$', login_required(Documento_list), name="documento_list"),
    url(r'^detalle/(?P<id_docum>\d+)$',login_required(Detalle_doc), name="documento_detalle"),
    url(r'^editar/(?P<id_documento>\d+)$',login_required(Documento_edit), name="documento_edit"),
    ]