from django.db import models

class Book(models.Model):
    id=models.CharField(max_length=250,primary_key=True)
    title=models.CharField(max_length=250, default="N/A")
    subtitle=models.CharField(max_length=250, default="N/A")
    authors=models.CharField(max_length=250, default="N/A")
    publisher=models.CharField(max_length=250, default="N/A")
    published_date=models.CharField(max_length=250,default="N/A")
    category=models.CharField(max_length=250, default="N/A")
    distribution_expense=models.FloatField(default=0)
    class Meta:
        db_table='Book'

