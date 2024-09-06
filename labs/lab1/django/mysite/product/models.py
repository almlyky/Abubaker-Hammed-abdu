from django.db import models

# Create your models here.
class Product(models.Model):
    pr_name=models.CharField(max_length=100)
    pr_price=models.IntegerField()
    
    def __str__(self):
        return self.pr_name
    
    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Products'  #name table
        # verbose_name_plural = 'ModelNames'