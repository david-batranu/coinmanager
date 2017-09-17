from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from coinmanager import serializers
from coinmanager import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = models.Investor.objects.all()
    serializer_class = serializers.InvestorSerializer


class BrokerViewSet(viewsets.ModelViewSet):
    queryset = models.Broker.objects.all()
    serializer_class = serializers.BrokerSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = models.Exchange.objects.all()
    serializer_class = serializers.ExchangeSerializer


class InvestorExchangeViewSet(viewsets.ModelViewSet):
    queryset = models.InvestorExchange.objects.all()
    serializer_class = serializers.InvestorExchangeSerializer


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = models.Symbol.objects.all()
    serializer_class = serializers.SymbolSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = models.Balance.objects.all()
    serializer_class = serializers.BalanceSerializer
