from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from phone_field import PhoneField

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=50,null=False,blank=True)
    lastName = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True,)
    city =  models.CharField(null=True,blank=True,max_length=25)
    country = models.CharField(null=True,blank=True,max_length=25)
    pin = models.CharField(max_length=10,null=True,blank=True)
    icon = models.URLField(max_length=1028,null=True,blank=True)
    emailId = models.EmailField(null=False,unique=True,blank=True)
    primaryContactNumber = PhoneField(null=True,blank=True)
    isMailVerified = models.BooleanField(default=False)
    isPhoneVerified = models.BooleanField(default=False)
    emailKey = models.CharField(null=True,blank=True,max_length=255)
    password = models.CharField(max_length=50,null=False,blank=False)
    otp = models.CharField(max_length=10,null=True,blank=True)
    otpGenTime = models.DateTimeField(auto_now=True)
    isRegisteredByGoogle = models.BooleanField(default=False)
    isRegisteredByFacebook = models.BooleanField(default=False)
    isRegisteredByApple= models.BooleanField(default=False)
    djangoUser = models.ForeignKey(User, null=True,blank=False, related_name='django_user',on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)	
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
                    if self.firstName != None and self.lastName != None:
                                    fullname = self.firstName+" "+self.lastName
                    else:
                                    fullname = self.pk
                    return str(fullname)


class Commodity(models.Model):
    
    MEASURING_UNITS = (('k','KILGOGRAM'),('g','gram'))
    PACKING_OPTIONS = (('c','CRATE'),('b','BAG'))
    
    name=models.CharField(null=False, max_length=200)
    description=models.CharField(null=True,max_length=1024)
    minimum_order_quantity=models.FloatField(default=1.0,blank=False,null=False)
    todays_price=models.FloatField(null=True)
    offer_price=models.FloatField(null=True)
    measuring_unit=models.CharField(null=False,max_length=100, default='Kg(s)', choices=MEASURING_UNITS)
    # discounted_price=models.FloatField(null=True)
    bulk_price=models.FloatField(null=True,blank=True)
    bulk_qty=models.FloatField(null=True,blank=True)
    available_quantity=models.FloatField(null=True)
    min_available_qty=models.FloatField(null=False,default=1.0)
    max_available_qty=models.FloatField(null=True,default=available_quantity)
    max_qty_allowed_per_order=models.FloatField(null=True,default=settings.MAX_QUANTITY_ALLOWED_PER_ORDER)
    gst=models.FloatField(null=False,default=0)
    isActive=models.BooleanField(default=True)
    quantityPerCrate=models.FloatField(null=True,blank=True)
    delivery_charge=models.FloatField(null=False,default=0.0)
    packingByCrateOrBag=models.CharField(null=False,max_length=100, default='Crate',choices=PACKING_OPTIONS)
    created=models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)+" "+str(self.todays_price)

