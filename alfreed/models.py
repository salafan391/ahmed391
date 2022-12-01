from django.db import models

# Create your models here.


class Workers(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Sales(models.Model):
    worker = models.ManyToManyField(Workers, blank=True)
    products = models.CharField(
        max_length=150, null=True, blank=True, default='لا يوجد')
    quantity = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)
    date_created = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    income = models.IntegerField(default=0)
    receipiant = models.ManyToManyField(Workers, related_name='receipiant')
    outcome = models.IntegerField(default=0)
    type = models.CharField(max_length=50, null=True, blank=True)
    person = models.ManyToManyField(Workers, related_name='person')

    def __str__(self):
        return str(self.products)

    class Meta:
        ordering = ['-created']
