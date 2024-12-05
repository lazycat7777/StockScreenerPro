from django.contrib import admin
from .models import IPAccess

@admin.register(IPAccess)
class IPAccessAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'expiration_date')
    search_fields = ('ip_address',)
    list_filter = ('expiration_date',)
