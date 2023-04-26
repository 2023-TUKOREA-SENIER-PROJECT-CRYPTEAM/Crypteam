from django.db import models

class BitCoin(models.Model):
    coin_name = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    news_registered_date = models.CharField(max_length=255)

class Ethereum(models.Model):
    coin_name = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    news_registered_date = models.CharField(max_length=255)

class EthereumClassic(models.Model):
    coin_name = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    news_registered_date = models.CharField(max_length=255)

class XRP(models.Model):
    coin_name = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    news_registered_date = models.CharField(max_length=255)

class CardanoADA(models.Model):
    coin_name = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)
    news_registered_date = models.CharField(max_length=255)


    class Meta:
        pass
        # using = 'other'
