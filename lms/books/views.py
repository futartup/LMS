from rest_framework import viewsets

from .serializers import BooksSerializer
from .models import Books
from rest_framework.permissions import IsAuthenticated


class BooksViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated, )
    queryset = Books.objects.all().order_by('title')
    serializer_class = BooksSerializer
