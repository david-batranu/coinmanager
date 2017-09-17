""" Admin.
"""
from django.contrib import admin
from coinmanager import models

REGISTER = (
    models.Symbol,
    models.Exchange,
    models.Balance,
    models.ExchangeSecrets,
    # models.Portfolio,
)

for model in REGISTER:
    admin.site.register(model)


class PortfolioExchangeInline(admin.TabularInline):
    """ Inline display of portfolio exchanges.
    """
    model = models.ExchangeSecrets
    extra = 0


class BalanceInline(admin.TabularInline):
    """ Inline display of portfolio funds.
    """
    model = models.Balance


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """ Extend Portfolio to include exchanges and balances.
    """
    inlines = [
        PortfolioExchangeInline,
        BalanceInline
    ]
