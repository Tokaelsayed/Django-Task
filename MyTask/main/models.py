from django.db import models

# Create your models here.
class dataset(models.Model):
    id = models.CharField(("Id"),primary_key=True,max_length=200)
    date_account_created = models.DateField(("date_account_created"),auto_now=True)
    timestamp_first_active = models.BigIntegerField(("timestamp_first_active"))
    date_first_booking = models.DateField(("date_first_booking"),auto_now=True)
    gender = models.CharField(("gender"),max_length=7)
    age = models.IntegerField(("age"))
    signup_method = models.CharField(("signup_method"),max_length=200)
    signup_flow = models.CharField(("signup_flow"),max_length=200)
    language = models.CharField(("language"),max_length=200)
    affiliate_channel = models.CharField(("affiliate_channel"),max_length=200)
    affiliate_provider = models.CharField(("affiliate_provider"),max_length=200)
    first_affiliate_tracked = models.CharField(("first_affiliate_tracked"),max_length=200)
    signup_app = models.CharField(("signup_app"),max_length=200)
    first_device_type = models.CharField(("first_device_type"),max_length=200)
    first_browser = models.CharField(("first_browser"),max_length=200)
    country_destination = models.CharField(("country_destination"),max_length=200)

    def __str__(self):
     return self.gender
