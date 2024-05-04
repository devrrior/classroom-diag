from rest_framework import serializers

from .models import Student

class SubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Student
        fields = ('name',)

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name',)

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ('name', 'age', 'tutor', 'subjects', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')