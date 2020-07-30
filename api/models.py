from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    email_verified = models.BooleanField(default=False)
    phone_number_verified = models.BooleanField(default=False)
    email_verification_code = models.IntegerField(default=0)
    phone_number_verification_code = models.IntegerField(default=0)


class SingleOrder(models.Model):
    customer_id = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    order_string = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id
