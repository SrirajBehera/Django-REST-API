import re
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = (
      'name', 'age'
    )

    def __str__(self):
      return self.name