from django.contrib import admin
from .models import Product ,Test
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','catigory', 'active') #display the id, name, price and catigory fields in the admin list view
    list_display_links =('id','name') #make the id and name fields clickable in the admin list view

    list_editable = ('price','catigory', 'active') #enable the price and catigory fields to be edited in the admin list view


    search_fields = ('name','price') #enable the search functionality in the admin list view by searching the name and price fields

    list_filter = ('catigory', 'active') #enable the filter functionality in the admin list view by filtering the price, catigory and active fields
admin.site.register(Product, ProductAdmin)
admin.site.register(Test)
admin.site.site_header = 'SI Houssaini'
admin.site.site_title = 'SI Houssaini Admin Panel'