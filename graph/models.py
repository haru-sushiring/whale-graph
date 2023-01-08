from django.db import models

# Create your models here.

class Whale(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    amount = models.FloatField()
    price = models.FloatField()
    move = models.CharField(max_length=4)

    class Meta:
        managed = False
        #db_table = 'whale'
        db_table = 'whale_table'
