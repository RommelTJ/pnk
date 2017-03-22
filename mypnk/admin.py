from django.contrib import admin
from .models import Organization, PNKEmployee
from .forms import PNKEmployeeForm


class PNKEmployeeAdmin(admin.ModelAdmin):
    form = PNKEmployeeForm
    search_fields = ('user',)
    list_display = ('user',)
    save_on_top = True
    actions_on_bottom = False
    list_per_page = 10


admin.site.register(Organization)
admin.site.register(PNKEmployee, PNKEmployeeAdmin)
