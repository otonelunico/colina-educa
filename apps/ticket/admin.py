from django.contrib import admin

from apps.ticket.models import Ticket, Estado, Establecimiento, Tema
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Estado)
admin.site.register(Establecimiento)
admin.site.register(Tema)
