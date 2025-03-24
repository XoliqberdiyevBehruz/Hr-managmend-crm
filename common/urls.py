from django.urls import path

from common import views


urlpatterns = [
    path('vacancy/create/', views.VacancyCreateApiView.as_view()),
    path('vacancy/list/', views.VacancyListApiView.as_view()),
    path('vacancy/<uuid:id>/', views.VacancyDetailApiView.as_view()),
    path('vacancy/<uuid:id>/update/', views.VacancyUpdateApiView.as_view()),
    path('vacancy/<uuid:id>/delete/', views.VacancyDeleteApiView.as_view()),
    path('platform/', views.PlatformListApiView.as_view()),

    path('job-application/<uuid:id>/change/', views.JobApplicationUpdate.as_view()),
    path('job-application/list/', views.JobApplicationListApiView.as_view()),
]