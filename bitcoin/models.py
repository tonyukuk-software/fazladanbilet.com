from django.db import models

# Create your models here.
class Bitcoin_Price(models.Model):
    past_price = models.FloatField(null=True)

    def __unicode__(self):
        return self.past_price