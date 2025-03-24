from rest_framework import generics, permissions

from django_filters.rest_framework import DjangoFilterBackend

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