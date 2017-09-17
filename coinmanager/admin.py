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
    model = models.ExchangeSecrets
    extra = 0


class BalanceInline(admin.TabularInline):
    model = models.Balance


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        PortfolioExchangeInline,
        BalanceInline
    ]
