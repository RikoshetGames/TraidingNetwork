from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from traidingnet.models import Supplier
from traidingnet.paginators import TraidingNetworkPagination
from traidingnet.serializers.supplier import SupplierCreateSerializers, SupplierSerializers

from users.permissions import IsModerator, IsCreator


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    default_serializer = SupplierSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contact__state']
    permission_classes = [IsAuthenticated]
    pagination_class = TraidingNetworkPagination

    serializers = {
        'create': SupplierCreateSerializers,
        'update': SupplierCreateSerializers,
    }

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.owner = self.request.user
        new_obj.save()

    def get_queryset(self):
        user = self.request.user
        obj = super().get_queryset()
        return obj.filter(create_user=user)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action == ['create', 'list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsCreator | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsCreator]
        return [permission() for permission in self.permission_classes]