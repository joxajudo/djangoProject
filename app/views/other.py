from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.geocoders import Nominatim  # Install geopy if not already installed

from app.models import Category, Item, User, SubCategory, About, AboutCategory
from app.permission import IsAuthorOrReadOnly
from app.serializers.other import CategorySerializer, ItemSerializer, UserSerializer, SubCategorySerializer, \
    AboutSerializer, AboutCategorySerializer


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class AboutCategoryViewSet(ListAPIView):
    queryset = AboutCategory.objects.all()
    serializer_class = AboutCategorySerializer


class AboutViewSet(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    parser_classes = [MultiPartParser, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', 'country', 'city']


class ItemViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    parser_classes = [MultiPartParser, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', 'country', 'city']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItembyUserAPIView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Item.objects.filter(user=user).all()


# class CurrentUserView(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def get(self, request):
#         user = request.user
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
