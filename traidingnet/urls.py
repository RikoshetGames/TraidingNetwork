from rest_framework import routers

from traidingnet.apps import TraidingnetConfig
from traidingnet.views.contacts import ContactsViewSet
from traidingnet.views.product import ProductViewSet
from traidingnet.views.supplier import SupplierViewSet

app_name = TraidingnetConfig.name

router = routers.SimpleRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contacts', ContactsViewSet, basename='contacts')


urlpatterns = router.urls
