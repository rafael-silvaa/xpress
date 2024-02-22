from django.contrib import admin
from .models import Contact, Reservation

admin.site.register(Contact)
admin.site.register(Reservation)

admin.site.site_header = "Xpress"
admin.site.index_title = "Xpress Administração"
admin.site.site_title = "Xpress Admin"
