from rest_framework import viewsets

from .serializers import LibraryActivitySerializer
from .models import *
from rest_framework.permissions import IsAuthenticated


class LibraryActivityViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated, )
    queryset = LibraryActivities.objects.all()
    serializer_class = LibraryActivitySerializer






