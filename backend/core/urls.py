from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from app.views import ProductView

route = routers.DefaultRouter()
route.register('', ProductView, basename='productview')


urlpatterns = [
    path("admin/", admin.site.urls),

    # Third party apps
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
    path('products/', include(route.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
