from django.contrib import admin
from .models import Contact, Reservation
from django.contrib.auth.admin import UserAdmin


# class OrderUpdateAdmin(admin.ModelAdmin):
#     list_display = ('order_id', 'update_desc', 'timestamp')
#     list_filter = ['timestamp']

#     def has_delete_permission(self, request, obj=None):
#         return False


# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ('order_id', 'userId', 'name', 'email', 'timestamp')
#     list_filter = ['timestamp']

#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'category', 'price')
#     list_filter = ['category']
#     search_fields = ['product_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'email', 'timestamp')
    list_filter = ['timestamp']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactAdmin)
admin.site.register(Reservation)

admin.site.site_header = "Cá T'Espero"
admin.site.index_title = "Cá T'Espero Administração"
admin.site.site_title = "Cá T'Espero Admin"
