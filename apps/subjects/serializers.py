from rest_framework import serializers

from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()



    class Meta:
        model = Subject
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')