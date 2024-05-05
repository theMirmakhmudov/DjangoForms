from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    subject = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name