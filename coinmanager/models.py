""" Models
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class Symbol(models.Model):
    """ Symbols used to display coins.
    """
    key = models.CharField(max_length=10)
    label = models.CharField(max_length=10)

    def __str__(self):
        return '{} ({})'.format(self.label, self.key)


class Exchange(models.Model):
    """ Generic information about an exchange.
    """
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True)
    api_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    """ A user (investor) portfolio, managed by another user (broker).
    """
    investor = models.OneToOneField(User, related_name='portfolio') # type: User
    broker = models.ForeignKey(
        User, related_name='portfolios', null=True, blank=True)

    def __str__(self):
        investor = self.investor.username
        try:
            broker = self.broker.username
        except ObjectDoesNotExist:
            broker = 'Nobody'
        return 'Portfolio for {} managed by {}.'.format(investor, broker)


class ExchangeSecrets(models.Model):
    """ Secret keys for each portfolio exchange.
    """
    portfolio = models.ForeignKey(Portfolio, related_name='exchanges')
    exchange = models.ForeignKey(Exchange)

    api_key = models.CharField(max_length=255, blank=True)
    secret = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return 'Secrets for {} used by {}'.format(
            self.exchange.name,
            self.portfolio
        )


class Balance(models.Model):
    """ Storage for funds from various portfolio exchanges.
    """
    portfolio = models.ForeignKey(Portfolio, related_name='balances')
    exchange = models.ForeignKey(Exchange)

    amount = models.FloatField()
    symbol = models.ForeignKey(Symbol)

    def __str__(self):
        return '{} {} in {}'.format(
            self.amount,
            self.symbol.label,
            self.exchange.name
        )
