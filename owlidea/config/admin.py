from django.contrib import admin
from .models import Link,Sidebar
from owlidea.custom_site import custom_site
from owlidea.base_admin import BaseOwnerAdmin

# Register your models here.


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href','status', 'weight', 'create_time')
    fields = ('title', 'href', 'status', 'weight')



@admin.register(Sidebar, site=custom_site)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type','content', 'status', 'create_time')
    fields = ('title', 'display_type', 'content')


