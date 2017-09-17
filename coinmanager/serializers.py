from django.contrib.auth.models import User
from coinmanager import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class InvestorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Investor
        fields = ('user', 'portfolio')


class BrokerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        queryset=models.Broker.objects.all(),
        view_name='broker-detail'
    )
    class Meta:
        model = models.Broker
        fields = ('id', 'user', 'portfolios')


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Portfolio
        fields = ('investor', 'exchanges', 'balances')


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Exchange
        fields = ('name', 'url', 'api_url')


class InvestorExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InvestorExchange
        fields = ('exchange', 'api_key', 'secret')


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Balance
        fields = ('amount', 'symbol', 'exchange')


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Symbol
        fields = ('key', 'label')
