from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token_refresh'),

    path('department/list/', views.DepartmentListApiView.as_view()),
    path('department/create/', views.DepartmentCreateApiView.as_view()),
    path('department/<uuid:id>/delete/', views.DepartmentDeleteApiView.as_view()),
    path('department/<uuid:id>/update/', views.DepartmentUpdateApiView.as_view()),

    path('user/create/', views.UserCreateApiView.as_view()),
    path('user/list/', views.UserListApiView.as_view()),
    path('user/<uuid:id>/', views.UserDetailApiView.as_view()),
    path('user/<uuid:id>/delete/', views.UserDeleteApiView.as_view()),
    path('user/<uuid:id>/update/', views.UserUpdateApiView.as_view()),
]