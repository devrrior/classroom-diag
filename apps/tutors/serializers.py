from rest_framework import serializers

from .models import Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')