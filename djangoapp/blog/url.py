from rest_framework import routers

from blog.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)