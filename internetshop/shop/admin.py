from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(models.product, ProductAdmin)
