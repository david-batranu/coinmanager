from django.db import models
from django.contrib.auth.models import User


class Symbol(models.Model):
    key = models.CharField(max_length=10)
    label = models.CharField(max_length=10)

    def __str__(self):
        return '{} ({})'.format(self.label, self.key)


class Exchange(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    api_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class InvestorExchange(models.Model):
    exchange = models.ForeignKey(Exchange)
    api_key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)

    def __str__(self):
        return self.exchange.name


class Balance(models.Model):
    amount = models.FloatField()
    symbol = models.ForeignKey(Symbol)
    exchange = models.ForeignKey(Exchange)

    def __str__(self):
        return '{} {} in {}'.format(
            self.amount,
            self.symbol.label,
            self.exchange.name
        )


class Portfolio(models.Model):
    exchanges = models.ManyToManyField(InvestorExchange)
    balances = models.ManyToManyField(Balance)

    def __str__(self):
        return '{} coins in {} exchanges for {}'.format(
            self.balances.count(),
            self.exchanges.count(),
            Investor.objects.filter(portfolio=self).first()
        )


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.OneToOneField(Portfolio, related_name='investor')

    def __str__(self):
        return 'Investor: {}'.format(self.user.username)


class Broker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolios = models.ManyToManyField(Portfolio, related_name='broker')

    def __str__(self):
        return 'Broker: {}'.format(self.user.username)
