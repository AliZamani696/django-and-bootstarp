from django.contrib import admin
from .models import Category,Product




# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryName', 'CategoryParent', 'has_children')
    list_filter = ('CategoryParent', )
    search_fields = ('CategoryName',)
    
@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('ProductName', 'ProductCategory', 'ProductDescription',"ProductPrice")
    list_filter = ('ProductPrice','ProductCategory','ProductName' )
    search_fields = ('ProductName',)
    