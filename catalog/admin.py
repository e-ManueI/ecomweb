from django.contrib import admin
from catalog.forms import ProductAdminForm
from catalog.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    
    #sets values for how the admi site lists your products
    list_display = ('name', 'price', 'old_price', 'created_at',  'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    # TODO searchfield
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # TODO sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

# Register my product model with the admin site
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    #sets values for how the admi site lists your products
    list_display = ('name', 'created_at',  'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    # TODO searchfield
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    # TODO sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}

# Register my product model with the admin site
admin.site.register(Category, CategoryAdmin)
