from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import Contacts, Product, Supplier
from .serializers.supplier import SupplierCreateSerializers


@admin.action(description='Очистить задолженность')
def set_null_debt(ModelAdmin, request, queryset):
    """ Действие, очищающее задолженность (ставит поле debt=0). """
    queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_email', 'state', 'city', 'street', 'building', 'create_user')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'product_model', 'release_date', 'product_price', 'create_user')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller_name', 'seller_type', 'contact', 'product', 'supplier_name', 'debt',
                    'create_time', 'create_user')
    list_filter = ('contact__city', 'contact__state')
    actions = [set_null_debt]

    def save_model(self, request, obj, form, change):
        serializer = SupplierCreateSerializers(data=request.POST)
        if serializer.is_valid():
            obj.save()
        else:
            raise ValidationError(
                                  'Ошибка при создании компании. Проверьте следующие поля:'
                                  '"Тип продавца", "Уровень поставки", "Поставщик"'
                                  )
