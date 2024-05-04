from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Tutor
from .serializers import TutorSerializer

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)