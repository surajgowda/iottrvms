from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, default=1)
    ownerdetails = models.ForeignKey('randw.OwnerDetails', on_delete=models.CASCADE, null=True, default=None)


class ViolationList(models.Model):
    violation_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    act = models.CharField(max_length=100)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class OwnerDetails(models.Model):
    uuid = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='owner_pictures/', null=True, blank=True)
    aadhar_number = models.CharField(max_length=12)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    model_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year_of_manufacture = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VehicleViolationHistory(models.Model):
    uuid = models.ForeignKey('OwnerDetails', on_delete=models.CASCADE)  # Use 'CustomUser' instead of 'User'
    violation_date = models.DateField()
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2)
    violation_id = models.ForeignKey('ViolationList', on_delete=models.CASCADE)  # No need for quotes

class VehicleLocation(models.Model):
    uuid = models.ForeignKey('OwnerDetails', on_delete=models.CASCADE)  # Use 'CustomUser' instead of 'User'
    time = models.TimeField()
    date = models.DateField()
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Location for {self.uuid.username} at {self.date} {self.time}"

class VehicleAccident(models.Model):
    uuid = models.ForeignKey('OwnerDetails', on_delete=models.CASCADE)  # Use 'CustomUser' instead of 'User'
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    time = models.DateTimeField()

    def __str__(self):
        return f"Accident for {self.uuid.name} at {self.time}"

class Insurance(models.Model):
    uuid = models.ForeignKey('OwnerDetails', on_delete=models.CASCADE)  # Use 'CustomUser' instead of 'customuser'
    insurance_id = models.CharField(max_length=20)
    coverage_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.insurance_id

class RegistrationCertificate(models.Model):
    uuid = models.ForeignKey('OwnerDetails', on_delete=models.CASCADE)  # Use 'CustomUser' instead of 'customuser'
    chassis_number = models.CharField(max_length=17)
    engine_number = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    vehicle_category = models.CharField(max_length=50)
    seating_capacity = models.PositiveIntegerField()
    date_of_registration = models.DateField()
    date_of_expiry = models.DateField()
    driving_limit = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.chassis_number