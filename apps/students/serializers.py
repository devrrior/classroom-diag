from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'tutor', 'subjects', 'created_at', 'updated_at')
        read_only_fields = ('id', 'tutor', 'created_at', 'updated_at')