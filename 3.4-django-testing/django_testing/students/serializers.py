from rest_framework import serializers
from students.models import Course
from django.conf import settings

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        try:
            student_count = len(data.get('students'))
        except TypeError:
            student_count = 0
        if student_count > settings.MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError(f'Ошибка! Должно быть не более {settings.MAX_STUDENTS_PER_COURSE} '
                                                  'студентов на курсе!')
        return data
