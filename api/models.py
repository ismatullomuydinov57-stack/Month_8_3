from django.db import models


class ConstructionCompany(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    company=models.ForeignKey(ConstructionCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





