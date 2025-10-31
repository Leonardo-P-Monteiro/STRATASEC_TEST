from rest_framework import serializers
from course.models import Course
from registration.models import Registration
from training.models import Training
from resources.models import Resource
from student.models import Student


# COURSE SERIALIZER
class CourseSerializer(serializers.ModelSerializer):

    training = serializers.CharField(source='training.name', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'training', 'start_date', 'conclusion_date']

# REGISTRARION SERIALIZER
class RegistrationSerializer(serializers.ModelSerializer):

    student_name = serializers.CharField(source='student.user.username', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Registration
        fields = ['student', 'student_name', 'course', 'course_name',]

# RESOURCE SERIALIZER
class ResourceSerializer(serializers.ModelSerializer):

    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'course', 'course_name', 'type_resource', \
                  'previous_acess', 'draft',]

# STUDENT SERIALIZER
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'user', 'e_mail', 'phone',]