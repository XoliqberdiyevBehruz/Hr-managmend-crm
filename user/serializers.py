from rest_framework import serializers

from user import models 


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['name']


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'department', 'address', 'job_title', 'joined_date', 'salary',
            'gender', 'date_of_birth', 'employment_type', 'contact', 'note', 'profile_image'
        ]        


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone', 'department', 'address', 'job_title', 'joined_date', 'salary',
            'gender', 'date_of_birth', 'employment_type', 'contact', 'note', 'profile_image'
        ]        