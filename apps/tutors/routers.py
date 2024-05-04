from rest_framework import routers

from .views import TutorsViewSet

router = routers.DefaultRouter()
router.register(r'tutors', TutorsViewSet, basename='tutors')