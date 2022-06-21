from .models import Test
from rest_framework import viewsets, permissions
from .serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestSerializer