from django.contrib import admin

from gallery.models import Category, Image, Location

# Register your models here.

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
