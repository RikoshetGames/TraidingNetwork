from rest_framework import serializers

from traidingnet.models import Supplier
from traidingnet.serializers.contacts import ContactsSerializer
from traidingnet.serializers.product import ProductSerializers
from traidingnet.validators import SupplierNetworkValidator


class SupplierCreateSerializers(serializers.ModelSerializer):
    """ Класс сериализатора cоздания поставщика """

    supply_level = serializers.IntegerField(required=False)

    class Meta:
        model = Supplier
        fields = ['sup_name', 'supplier_type', 'supply_level', 'contact', 'product', 'supplier_name', 'debt']
        validators = [SupplierNetworkValidator()]

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['create_user'] = request.user

        if validated_data.get('supplier_name'):
            supplier_name = validated_data['supplier_name']
            validated_data['supply_level'] = supplier_name.supply_level + 1
        elif validated_data.get('supplier_type') == 0:
            validated_data['supply_level'] = 0

        return super().create(validated_data)


class SupplierSerializers(serializers.ModelSerializer):
    """ Класс сериализатора поставщика """
    contact = ContactsSerializer()
    product = ProductSerializers()

    supplier_type = serializers.CharField(source='get_supplier_type_display')

    class Meta:
        model = Supplier
        fields = '__all__'