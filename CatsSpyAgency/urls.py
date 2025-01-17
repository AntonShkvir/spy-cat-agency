from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SpyCat API",
        default_version="v1",
        description="API for managing SpyCat records",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cats.urls')),
    path('api/', include('missions.urls')),
    path('api/', include('notes.urls')),
    path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),

]
