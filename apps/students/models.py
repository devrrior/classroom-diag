from django.db import models
from apps.tutors.models import Tutor
from apps.subjects.models import Subject

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='students', null=True)
    subjects = models.ManyToManyField(Subject, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name