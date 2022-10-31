from django.urls import path, include
# from .views import GetAllInfoUserView, RegisterUserView, AddProffesionView, AddInfoUserView

from user.views import UserViewSet, InfoViewSet, ProfessionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'info', InfoViewSet, basename='info')
router.register(r'profession', ProfessionViewSet, basename='profession')

urlpatterns = router.urls
