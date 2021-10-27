from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)

