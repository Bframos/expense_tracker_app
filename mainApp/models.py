from django.db import models

class Book(models.Model):
    
    title=models.CharField(("title"),max_length=255)
    subtitle=models.CharField(("subtitle"),max_length=255)
    authors=models.CharField(("authors"),max_length=255)
    published_date=models.DateField(("published_date"),auto_now=True)
    category=models.CharField(("category"),max_length=255)
    distribution_expense=models.FloatField(("distribution_expense"),default=0)






