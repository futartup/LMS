from rest_framework import routers
from .views import *

book_router = routers.DefaultRouter()

book_router.register("books", BooksViewSet)

