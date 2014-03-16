from django.db import models

# Create your models here.
class asset(models.Model):
    asset_id = models.CharField(max_length = 50)
    asset_name = models.CharField(max_length = 50)
    purchase_date = models.DateTimeField()
    asset_type = models.CharField(max_length = 50)
    asset_role = models.CharField(max_length = 50)
    asset_own = models.CharField(max_length = 50)
    asset_content = models.CharField(max_length = 50)
    asset_event = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.asset_name

class type(models.Model):
    name = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50)
    standard = models.CharField(max_length = 50)
    
class role(models.Model):
    role_nmae = models.CharField(max_length = 50)

class contact(models.Model):
    name = models.CharField(max_length = 50)
    number = models.IntegerField()
