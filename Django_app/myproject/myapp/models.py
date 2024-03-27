from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myapp'

class ElectricityBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reading = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.customer.name} - {self.date}"

    class Meta:
        app_label = 'myapp'
