from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register("products",views.ProductGenericViewSet,basename="crud_operation")
# print(router.urls)
urlpatterns=router.urls