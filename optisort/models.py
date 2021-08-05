from django.db import models


class SortList(models.Model):
    name = models.CharField(max_length=255)
    lang = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "SortList"
        verbose_name = "SortList"


class SortListItem(models.Model):
    sortlist = models.ForeignKey(SortList, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.number


class ParameterFile(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(
        max_length=255,
        choices=(
            ("green", "Green"),
            ("white", "White"),
        ),
    )
    sortlist = models.ForeignKey(SortList, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Parameters"
        verbose_name = "Parameter"

    def __str__(self) -> str:
        return self.name
