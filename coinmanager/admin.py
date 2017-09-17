from django.contrib import admin
from coinmanager import models

REGISTER = (
    models.Symbol,
    models.Exchange,
    models.InvestorExchange,
    models.Balance,
    models.Portfolio,
    models.Investor,
    models.Broker,
)

for model in REGISTER:
    admin.site.register(model)