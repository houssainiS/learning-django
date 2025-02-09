from django.contrib import admin
from .models import Product ,Test
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','catigory') #display the id, name, price and catigory fields in the admin list view
    list_display_links =('id','name') #make the id and name fields clickable in the admin list view

admin.site.register(Product, ProductAdmin)
admin.site.register(Test)
admin.site.site_header = 'SI Houssaini'
admin.site.site_title = 'SI Houssaini Admin Panel'