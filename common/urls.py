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

    path('payment/list/', views.PaymentListApiView.as_view()),
    path('payment/change/<uuid:id>/', views.PaymentChangeApiView.as_view()),
    path('payment/statistics/', views.PaymentStatisticsApiView.as_view()),

    path('department/statistics/', views.DepartmentStatisticsApiView.as_view()),
]