from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
   exclude = ['id']
   readonly_fields = ('created_at', 'updated_at',)
   list_display = ['id', 'name', 'description', 'price', 'stock_quantity', 'created_at', 'updated_at']

#    fieldsets = (
#         (None, {
#             'fields': ('name', 'description', 'price', 'stock_quantity')
#         }),
#         ('Timestamps', {
#             'fields': ('created_at', 'updated_at')
#         }),
#     )

class ProductDetailAdmin(admin.ModelAdmin):
     exclude = ['id']
     list_display =['id', 'product', 'warranty_period', 'specifications', 'weight', 'manufacturer']



admin.site.register(Product,ProductAdmin)
admin.site.register(ProductDetail,ProductDetailAdmin)