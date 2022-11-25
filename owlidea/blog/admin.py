from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .adminforms import PostAdminForm
from .models import Tag, Post, Category

# Register your models here.
from owlidea.custom_site import custom_site


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline,]
    list_display = ('name', 'status', 'is_nav','create_time','post_count')
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status', 'create_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'category', 'status', 'create_time', 'owner', 'operator')
    list_display_link = []
    list_filter = [CategoryOwnerFilter,'category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    action_on_bottom = True

    # 编辑
    save_on_top = False

    exclude = ('owner',)
    # filter_horizontal = ('tags',)
    filter_vertical = ('tags',)
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tags',
    # )
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields' : (
                ('title', 'category'),
                'status'
            )
        }),
        ('内容',{
            'fields' : (
                'desc',
                'content',
            )
        }),
        ('额外信息',{
            'classes' : ('collapse',),
            'fields' : (
                'tags',
            )
        })
    )

    def operator(self,obj):
        return format_html(
            '<a href="{}">编辑<a/>',
            reverse('cus_admin:blog_post_change', args=[obj.id])
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self,request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),}
        js = ("https://cdn.bootcss.com/bootsrap/4.0.0-beta.2/js/bootstrap.min.js",)

