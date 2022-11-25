from django.contrib import admin
from .models import Link,Sidebar
from owlidea.custom_site import custom_site

# Register your models here.

@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href','status', 'weight', 'create_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(Link).save_model(request, obj, form, change)


@admin.register(Sidebar, site=custom_site)
class SidebarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type','content', 'status', 'create_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(Sidebar).save_model(request, obj, form, change)

