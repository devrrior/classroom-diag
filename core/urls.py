from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from apps.tutors.routers import router as tutors_router
from apps.students.routers import router as students_router
from apps.subjects.routers import router as subjects_router
from .patches import DefaultRouter

app_router = DefaultRouter()
app_router.extend(tutors_router)
app_router.extend(students_router)
app_router.extend(subjects_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(app_router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
