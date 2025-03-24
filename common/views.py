from rest_framework import generics, permissions
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from user.models import Department 
from common import models, serializers, filters


class VacancyCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy
    permission_classes = (permissions.IsAuthenticated, )



class VacancyListApiView(generics.ListAPIView):
    serializer_class = serializers.VacancyListSerializer
    queryset = models.Vacancy.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    

class VacancyUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'    


class VacancyDeleteApiView(generics.DestroyAPIView):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'    


class VacancyDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'    


class PlatformListApiView(generics.ListCreateAPIView):
    serializer_class = serializers.PlatformListSerializer
    queryset = models.Platform.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class JobApplicationUpdate(generics.UpdateAPIView):
    serializer_class = serializers.JobApplicationChangeSerializer
    queryset = models.JobApplication
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'id'


class JobApplicationListApiView(generics.ListAPIView):
    serializer_class = serializers.JobApplicationListSerializer
    queryset = models.JobApplication.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class PaymentListApiView(generics.ListAPIView):
    serializer_class = serializers.PaymentListSerializer
    queryset = models.Payment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.PaymentFilter


class PaymentChangeApiView(generics.UpdateAPIView):
    serializer_class = serializers.PaymentChangeSerializer
    queryset = models.Payment
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'


class PaymentStatisticsApiView(generics.GenericAPIView):
    serializer_class = None 

    def get(self, request):
        payments = models.Payment.objects.all()
        total_salary = sum(payment.salary for payment in payments)
        average_salary = total_salary / payments.count()
        return Response({
            'total_salary': total_salary,
            'average_salary': average_salary,
            'paid_payment': payments.filter(status='paid').count(),
            'unpaid_payment': payments.filter(status='unpaid').count(),
        })


class DepartmentStatisticsApiView(generics.ListAPIView):
    serializer_class = serializers.DepartmentStatisticsSerializer
    queryset = Department.objects.all()
