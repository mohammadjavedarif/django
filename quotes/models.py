from django.db import models

# Create your models here.

class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    quote_category =models.ForeignKey(
        'QuoteCategory', 
        on_delete = models.CASCADE
    )