from django.contrib import admin
from .models import *
# Register your models here.
class SubscriberAdmin (admin.ModelAdmin):
    #list_display = ["name","email"]
    list_display = [field.name for field in Subscriber._meta.fields]
    search_fields = ["name", "email"]
    
    #inlines = [FieldMappingInline]
    #list_filter = ["name"]
    #fields = ["email"]
    #exclude = ["email"]
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
