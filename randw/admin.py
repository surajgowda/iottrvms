from django.contrib import admin
from .models import VehicleViolationHistory, ViolationList, OwnerDetails, VehicleLocation, VehicleAccident, Insurance, RegistrationCertificate
from .models import CustomUser  # Replace with your actual user model

admin.site.register(CustomUser)
admin.site.register(ViolationList)
admin.site.register(OwnerDetails)
admin.site.register(VehicleLocation)
admin.site.register(VehicleAccident)
admin.site.register(Insurance)
admin.site.register(RegistrationCertificate)
admin.site.register(VehicleViolationHistory)



