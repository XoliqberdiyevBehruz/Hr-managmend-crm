from rest_framework import serializers

from common import models


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


