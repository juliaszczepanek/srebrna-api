from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
