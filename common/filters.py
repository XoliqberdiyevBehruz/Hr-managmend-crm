import django_filters 

from common import models 

class FilterJobApplication(django_filters.FilterSet):
    class Meta:
        model = models.JobApplication
        fields = ['status']
    

class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = models.Payment
        fields = ['status', 'employee__first_name', 'employee__last_name']