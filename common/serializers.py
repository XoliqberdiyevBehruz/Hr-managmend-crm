from rest_framework import serializers

from common import models
from user.models import User, Department


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = ['name']


class PlatformListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = ['id', 'name']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy

        fields = [
            'job_title', 'short_description', 'full_description', 'platforms', 'post_date', 
        ]


class VacancyListSerializer(serializers.ModelSerializer):
    platforms = PlatformListSerializer(many=True, read_only=True)

    class Meta:
        model = models.Vacancy
        fields = [
            'id', 'job_title', 'short_description', 'full_description', 'platforms', 'post_date', 'status' 
        ]


class JobApplicationChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobApplication
        fields = [
            'status'
        ]


class JobApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobApplication
        fields = [
            'id', 'name', 'contact', 'apllied_from', 'date', 'status'
        ]


class UserPaymentSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField(method_name='get_department')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'department', 'phone', 'salary']

    def get_department(self, obj):
        return obj.department.name if obj.department else None

class PaymentListSerializer(serializers.ModelSerializer):
    employee = UserPaymentSerializer()
    class Meta:
        model = models.Payment
        fields = [
            'id', 'employee', 'salary', 'status' 
        ]

    
class PaymentChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            'status'
        ]

    
class DepartmentStatisticsSerializer(serializers.ModelSerializer):
    employees_count = serializers.SerializerMethodField(method_name='get_employees_count')
    class Meta:
        model = Department
        fields = [
            'id', 'name', 'employees_count'
        ]

    def get_employees_count(self, obj):
        return obj.users.count()
    