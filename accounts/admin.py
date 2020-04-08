from django.contrib import admin

from .models import *
admin.site.register(Usuario)
admin.site.register(Empleo)
admin.site.register(Tag)
admin.site.register(Recibo)