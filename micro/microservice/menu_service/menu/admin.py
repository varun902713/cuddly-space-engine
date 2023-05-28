from django.contrib import admin

# Register your models here.
from .models import Restaurant,Category,Menu,MenuItem

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(MenuItem)