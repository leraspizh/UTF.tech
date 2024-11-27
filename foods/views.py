from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Food,FoodCategory
from .serializers import FoodSerializer,FoodListSerializer



class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        )
        return queryset


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



