from django.contrib import admin
from sitesettings.models import Settings, SettingsGroup

class SettingsInline(admin.TabularInline):
    model = Settings
    fields = ['value']
    extra = 0

class SettingsGroupAdmin(admin.ModelAdmin):
    readonly_fields = ['code', 'name']
    inlines = [SettingsInline, ]

    def has_add_permission(self, request):
        return False

admin.site.register(SettingsGroup, SettingsGroupAdmin)