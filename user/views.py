from rest_framework import generics, permissions, parsers

from user import models, serializers


class DepartmentCreateApiView(generics.CreateAPIView):
    queryset = models.Department
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

class DepartmentListApiView(generics.ListAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentUpdateApiView(generics.UpdateAPIView):
    queryset = models.Department
    serializer_class = serializers.DepartmentSerializer
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated, )


class DepartmentDeleteApiView(generics.DestroyAPIView):
    queryset = models.Department
    serializer_class = serializers.DepartmentSerializer
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated,)



class UserCreateApiView(generics.CreateAPIView):
    queryset = models.User
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)


class UserListApiView(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserUpdateApiView(generics.UpdateAPIView):
    queryset = models.User
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)


class UserDeleteApiView(generics.DestroyAPIView):
    queryset = models.User
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'


class UserDetailApiView(generics.RetrieveAPIView):
    queryset = models.User
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
