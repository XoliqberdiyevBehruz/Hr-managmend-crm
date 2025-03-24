from django_filters.rest_framework import FilterSet

from common import models 

class FilterJobApplication(FilterSet):
    class Meta:
        model = models.JobApplication
        fields = ['status']