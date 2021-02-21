from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from .models import Product, Seller, Tags, Category
from ckeditor.widgets import CKEditorWidget


# Register your models here.
class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("tags",)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
