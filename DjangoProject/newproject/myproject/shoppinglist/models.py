from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    shop_site = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    item_url = models.URLField(blank=True,null=True)
    count = models.PositiveBigIntegerField(default=0)
    buy_date = models.DateField(blank=True,null=True)
    shop = models.ForeignKey(Shop,blank=True,null=True,verbose_name='shop',on_delete=models.PROTECT)
    buy = models.BooleanField(default=False)
    
    def __str__(self):
        return '{} ({})'.format(self.name,self.buy_date)