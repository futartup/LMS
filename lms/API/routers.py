from rest_framework import routers
from books.routers import book_router
from library.routers import library_router


class FullRoutes(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)


api_router = FullRoutes()

api_router.extend(book_router)
api_router.extend(library_router)
