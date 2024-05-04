from rest_framework import routers

from apps.subjects.views import SubjectViewSet

router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet)