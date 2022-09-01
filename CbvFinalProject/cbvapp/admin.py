from django.contrib import admin
from cbvapp.models import Cloth
# Register your models here.
class ClothAdmin(admin.ModelAdmin):
    list_display=['name', 'color', 'size', 'price']
admin.site.register(Cloth, ClothAdmin)
