from django.contrib import admin

from .models import Category, Product,Subcategory

admin.site.register(Category)
admin.site.register(Subcategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','user','price', 'category','condition']
    search_fields = ['user__username', 'title', 'condition']






#admin.site.register(OrderItem)
#admin.site.register(Order)