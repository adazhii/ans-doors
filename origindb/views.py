from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from origindb.models import Inventre, Invendet, Inventry
from origindb.serializers import CategorySerializer, ComponentSerializer, ProductSerializer


class CategoriesAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Inventre.objects.filter()
    # permission_classes = (IsAuthenticated,)
    pagination_class = None


class ComponentsAPIView(generics.ListAPIView):
    serializer_class = ComponentSerializer
    queryset = Invendet.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = None


class ProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Inventry.objects.filter(origin_category__origin_child_tree_id='    4').exclude(id__contains='($)').select_related('origin_category')
    pagination_class = None
