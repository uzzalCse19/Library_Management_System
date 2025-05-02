from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger config

schema_view = get_schema_view(
   openapi.Info(
      title="Library Management API",
      default_version='v1',
      description="API for managing library books and members",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@Lib_MS.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Library app API
    path('api/', include('library.urls')),

    # Auth
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/token/', include('users.urls')),  # Use separate path for JWT obtain/refresh

    # DRF browsable login
    path('api-auth/', include('rest_framework.urls')),

    # Swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + debug_toolbar_urls()

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)