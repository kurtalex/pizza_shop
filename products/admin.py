from django.contrib import admin
from .models import *
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

    # class ProductCategoryAdmin(admin.ModelAdmin):
    #     list_display = [field.name for field in ProductCategory._meta.fields]
    #
    #     class Meta:
    #         model = ProductCategory

class ProductAdmin (admin.ModelAdmin):
    #list_display = ["name","email"]
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    # list_filter = ['name', 'id']
    # search_fields = ['name', 'id']
    #search_fields = ["name", "email"]
    #inlines = [FieldMappingInline]
    #list_filter = ["name"]
    #fields = ["email"]
    #exclude = ["email"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    #list_display = ["name","email"]
    list_display = [field.name for field in ProductImage._meta.fields]
    #search_fields = ["name", "email"]
    #inlines = [FieldMappingInline]
    #list_filter = ["name"]
    #fields = ["email"]
    #exclude = ["email"]
    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)