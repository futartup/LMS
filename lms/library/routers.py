from rest_framework import routers
from .views import *

library_router = routers.DefaultRouter()

library_router.register("library", LibraryActivityViewSet)

