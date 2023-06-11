from django.contrib import admin
from .models import Site, Action

admin.site.register(Site)


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('action_id', 'timestamp', 'user_id', 'site', 'action_type', 'page_id')
    list_filter = ('action_type',)
    search_fields = ('user_id', 'site__name', 'page_id')
