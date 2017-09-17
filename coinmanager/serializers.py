""" Serializers needed for the REST API.
"""

from django.contrib.auth.models import User
from coinmanager import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'portfolio', 'portfolios')


class SymbolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Symbol
        fields = ('key', 'label')


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Exchange
        fields = ('name', 'url', 'api_url')


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='portfolio-detail'
    )

    class Meta:
        model = models.Portfolio
        fields = ('id', 'investor', 'broker', 'balances')


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Balance
        fields = ('portfolio', 'exchange', 'amount', 'symbol')
