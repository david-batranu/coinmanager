""" Views.
"""

from django.contrib.auth.models import User
from rest_framework import viewsets

from coinmanager import serializers
from coinmanager import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = models.Exchange.objects.all()
    serializer_class = serializers.ExchangeSerializer


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = models.Symbol.objects.all()
    serializer_class = serializers.SymbolSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = models.Balance.objects.all()
    serializer_class = serializers.BalanceSerializer
