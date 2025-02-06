from django.contrib import admin
from .models import Product ,Test
# Register your models here.
admin.site.register(Product)
admin.site.register(Test)
admin.site.site_header = 'SI Houssaini'
admin.site.site_title = 'SI Houssaini Admin Panel'