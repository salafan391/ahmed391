from django.db import models

# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
class Sales(models.Model):
    worker = models.ManyToManyField(Workers)
    products = models.CharField(max_length=150,null=True)
    quantity = models.IntegerField()
    paid = models.IntegerField()
    date_created = models.DateTimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.products)
    class Meta:
        ordering = ['-created']


class Incomes(models.Model):
    income = models.IntegerField()
    receipiant = models.ManyToManyField(Workers)
    created = models.DateTimeField(auto_now_add=True)
    sales = models.ForeignKey(Sales,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.income)

class Outcomes(models.Model):
    outcome = models.IntegerField()
    type = models.CharField(max_length=50,null=True)
    person = models.ManyToManyField(Workers)
    created = models.DateTimeField(auto_now_add=True)
    sales = models.ForeignKey(Sales,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.outcome)
