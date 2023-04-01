from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"documents", views.DocumentViewset, basename="documents")

urlpatterns =  router.urls
