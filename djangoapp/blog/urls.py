from rest_framework import routers

from rest_framework import routers

from blog.views import CategoryViewSet, NewsViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('news', NewsViewSet)
urlpatterns = router.urls
