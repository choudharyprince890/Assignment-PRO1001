from django.db import models


class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.date} - {self.description}"
