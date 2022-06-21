from django.contrib import admin
from .models import Test


# Register your models here.

class AppTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'time', 'status', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_editable = ('status', 'done')
    list_filter = ('done',)


admin.site.register(Test, AppTestAdmin)

