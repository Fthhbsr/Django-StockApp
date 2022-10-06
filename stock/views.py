from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

# from .permissions import ProductManagerPermission
from .models import (
    Category, 
    TransactionStock,
    Brand, 
    Firm, 
    Product)
from .serializers import (
    TransactionStockSerializer, 
    CategorySerializer, 
    BrandSerializer, 
    FirmSerializer, 
    ProductSerializer)

# Create your views here.

class TransactionStockView(viewsets.ModelViewSet):
    queryset = TransactionStock.objects.all()
    serializer_class = TransactionStockSerializer
    permission_classes = [DjangoModelPermissions]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [DjangoModelPermissions]


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [DjangoModelPermissions]

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]