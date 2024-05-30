from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from traidingnet.models import Product
from traidingnet.serializers.product import ProductSerializers
from users.permissions import IsModerator, IsCreator


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.creation_user = self.request.user
        new_obj.save()

    def get_permissions(self):
        if self.action == ['create', 'list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsCreator | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsCreator]
        return [permission() for permission in self.permission_classes]