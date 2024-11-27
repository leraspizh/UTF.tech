from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import FoodCategoryViewSet



router = SimpleRouter()
router.register('foods', FoodCategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]