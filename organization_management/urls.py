

from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from core.views import OrganizationViewSet, RoleViewSet, UserViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls'))

]
