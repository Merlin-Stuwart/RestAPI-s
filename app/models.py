from django.db import models

# Create your models here.
class productcategory(models.Model):
    categoryname=models.CharField(max_length=100,primary_key=True)
    categoryid=models.IntegerField()
    def __str__(self):
        return self.categoryname
class product(models.Model):
    categoryname=models.ForeignKey(productcategory,on_delete=models.CASCADE)
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productDate=models.DateField()
