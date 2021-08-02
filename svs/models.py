from django.db import models
from django.utils import timezone

MACHINES = (
    ("unknown", "Unknown"),
    ("weight_windows", "Windows WeightLine"),
    ("weight_plc", "PLC WeightLine"),
    ("sortline_windows", "Windows SortLine"),
    ("sortline_plc", "PLC SortLine"),
    ("gubbuncher", "Gub-Buncher"),
)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name


class Machine(models.Model):
    type = models.CharField(
        max_length=32, choices=MACHINES, null=False, default="unknown"
    )
    number = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    install_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.number
