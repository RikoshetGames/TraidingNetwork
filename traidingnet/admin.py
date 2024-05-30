from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import Contacts, Product, Supplier
from .serializers.supplier import SupplierCreateSerializers


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_email', 'state', 'city', 'street', 'building', 'create_user')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_model', 'release_date', 'product_price', 'create_user')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('sup_name', 'supplier_type', 'contact', 'product', 'supplier_name', 'debt',
                    'create_time', 'create_user')
    list_filter = ('contact__city', 'contact__state')

    def save_model(self, request, obj, form, change):
        serializer = SupplierCreateSerializers(data=request.POST)
        if serializer.is_valid():
            obj.save()
        else:
            raise ValidationError(
                                  'Ошибка при создании компании. Проверьте следующие поля:'
                                  '"Тип продавца", "Уровень поставки", "Поставщик"'
                                  )