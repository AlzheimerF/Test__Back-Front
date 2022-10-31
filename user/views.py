from .models import InfoUser, Profession
from .serializer import ProfessionSerializer, InfoUserSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def info(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.get(pk=kwargs.get('pk')))
        serializer1 = ProfessionSerializer(Profession.objects.get(prof_id=kwargs.get('pk')))
        serializer2 = InfoUserSerializer(InfoUser.objects.get(info_id=kwargs.get('pk')))
        return Response([serializer.data, serializer1.data, serializer2.data])

class InfoViewSet(viewsets.ModelViewSet):

    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializer

class ProfessionViewSet(viewsets.ModelViewSet):

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

    #
    # @action(detail=True, methods=['delete'])
    # def delete(self, request, *args, **kwargs):
    #     Profession.objects.get(prof_id=kwargs.get('pk')).delete()
    #     return Response('Успех')

# class GetAllInfoUserView(generics.RetrieveAPIView):
#
#     def get(self, request, *args, **kwargs):
#         serializer = UserSerializer(User.objects.get(pk=kwargs.get('pk')))
#         serializer1 = ProffesionSerializer(Profession.objects.get(prof_id=kwargs.get('pk')))
#         serializer2 = InfoUserSerializer(InfoUser.objects.get(info_id=kwargs.get('pk')))
#         return Response([serializer.data, serializer1.data, serializer2.data])
#
# class RegisterUserView(generics.CreateAPIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class AddProffesionView(generics.CreateAPIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = ProffesionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# class AddInfoUserView(generics.CreateAPIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = InfoUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
