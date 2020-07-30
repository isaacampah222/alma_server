from rest_framework.generics import GenericAPIView
from rest_framework import mixins, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import SingleOrder
from knox.views import LoginView as KnoxLoginView
from .serializers import SingleOrderSerializer,UserSerializer,RegisterSerializer

class SingleOrderView(GenericAPIView, mixins.CreateModelMixin,mixins.ListModelMixin,
mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = SingleOrder.objects.all()
    serializer_class = SingleOrderSerializer
    lookup_field = 'id'

    def get(self, request, id= None):
        if id: 
            return self.retrieve(request, id)
        else:
            return self.list(request)


    def post(self, request):
        return self.create(request)

    def delete(self, request, id):
        return self.destroy(request, id)


class RegisterAPI(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=  None):
        serializer =AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)