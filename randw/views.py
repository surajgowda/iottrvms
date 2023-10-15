import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import OwnerDetails,User,Insurance,RegistrationCertificate,VehicleAccident,VehicleLocation,VehicleViolationHistory, ViolationList
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser
from django.contrib import messages
from .models import RegistrationCertificate, OwnerDetails
from django.shortcuts import render
from .models import OwnerDetails, VehicleViolationHistory, Insurance, RegistrationCertificate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VehicleLocation
from .serializers import VehicleLocationSerializer


def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@api_view(['POST'])
def save_vehicle_location(request):
    if request.method == 'POST':
        serializer = VehicleLocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def user(request):
    user_id = request.user.id  # Get the user's ID

    # Retrieve the owner details associated with the user
    owner_details = OwnerDetails.objects.filter(uuid=user_id)

    # Retrieve vehicle violation history for the user
    violations = VehicleViolationHistory.objects.all()

    # Retrieve insurance details for the user
    insurance_details = Insurance.objects.all()

    # Retrieve registration details for the user
    registration_details = RegistrationCertificate.objects.all()
    print(violations, insurance_details)
    # Pass the data to the template
    return render(request, 'dashboard.html', {
        'violation_data': violations,
        'owner_details_data': owner_details,
        'insurance_data': insurance_details,
        'registration_data': registration_details,
    })


def police(request):
    violations = VehicleViolationHistory.objects.all()
    return render(request, "police.html", {'violations': violations})

def violationlist(request):
    violationlist = ViolationList.objects.all()
    return render(request, 'violationlist.html', {'vio':violationlist})

def hospital(request):
    accidents = VehicleAccident.objects.all() 
    return render(request, 'hospital.html', {'accidents': accidents})

def service(request):
    return render(request,'service.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Create a new user object
            user = CustomUser.objects.create_user(username, email, password)
            user.save()
            # Redirect to a success page or do any other desired actions
            return redirect('login')  # Replace with your success page URL
        else:
            # Handle password mismatch error
            return render(request, 'Registration.html', {'error_message': 'Passwords do not match'})
    return render(request, 'Registration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user has filled out OwnerDetails
            if not user.ownerdetails:
                return redirect('ownerdetails')  # Redirect to OwnerDetails form
            return redirect('user')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def ownerdetails(request):
    # Get the currently logged-in user
    user = request.user

    if request.method == 'POST':
        # Capture form data
        name = request.POST.get('name')
        picture = request.FILES.get('picture')
        aadhar_number = request.POST.get('aadhar_number')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        model_name = request.POST.get('model_name')
        color = request.POST.get('color')
        year_of_manufacture = request.POST.get('year_of_manufacture')
        manufacturer = request.POST.get('manufacturer')

        if user.ownerdetails is None:
            # If not, create a new OwnerDetails object
            owner_details = OwnerDetails(
                uuid=user.id,
                name=name,
                picture=picture,
                aadhar_number=aadhar_number,
                contact_number=contact_number,
                address=address,
                model_name=model_name,
                color=color,
                year_of_manufacture=year_of_manufacture,
                manufacturer=manufacturer
            )
            owner_details.save()
            user.ownerdetails = owner_details
            user.save()
            
        else:
            # Update the existing OwnerDetails record
            user.ownerdetails.name = name
            user.ownerdetails.picture = picture
            user.ownerdetails.aadhar_number = aadhar_number
            user.ownerdetails.contact_number = contact_number
            user.ownerdetails.address = address
            user.ownerdetails.model_name = model_name
            user.ownerdetails.color = color
            user.ownerdetails.year_of_manufacture = year_of_manufacture
            user.ownerdetails.manufacturer = manufacturer
            user.ownerdetails.save()
            
        # Add a success message
        messages.success(request, 'Details updated successfully')
    else:
        return render(request, 'ownerdetails.html') 
    return render(request, 'ownerdetails.html')



def registrationcert(request):
    if request.method == 'POST':
        # Get the user's UUID from the session or any other source
        uuid = request.user.id  # Replace with the actual method of getting the user's UUID
        chassis_number = request.POST.get('chassis_number')
        engine_number = request.POST.get('engine_number')
        vehicle_type = request.POST.get('vehicle_type')
        fuel_type = request.POST.get('fuel_type')
        vehicle_category = request.POST.get('vehicle_category')
        seating_capacity = request.POST.get('seating_capacity')
        date_of_registration = request.POST.get('date_of_registration')
        date_of_expiry = request.POST.get('date_of_expiry')
        driving_limit = request.POST.get('driving_limit')

        # Get the associated OwnerDetails instance
        owner_details = OwnerDetails.objects.get(uuid=uuid)

        # Create a new RegistrationCertificate object associated with the OwnerDetails and save it
        registration_certificate = RegistrationCertificate(
            uuid=owner_details,
            chassis_number=chassis_number,
            engine_number=engine_number,
            vehicle_type=vehicle_type,
            fuel_type=fuel_type,
            vehicle_category=vehicle_category,
            seating_capacity=seating_capacity,
            date_of_registration=date_of_registration,
            date_of_expiry=date_of_expiry,
            driving_limit=driving_limit
        )
        registration_certificate.save()

        # Redirect to a success page or do any other desired actions
        return redirect('user')  # Replace 'success_page' with your success page URL

    return render(request, 'registration_certificate_form.html')

from django.shortcuts import render, redirect
from .models import OwnerDetails, Insurance

def insurance(request):
    if request.method == 'POST':
        # Get the user's UUID from the logged-in user
        uuid = request.user.id  # Use request.user.id to get the user's ID
        insurance_id = request.POST.get('insurance_id')
        coverage_type = request.POST.get('coverage_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        insurance_coverage_amount = request.POST.get('insurance_coverage_amount')

        # Get the associated OwnerDetails instance
        owner_details = OwnerDetails.objects.get(uuid=uuid)

        # Create a new Insurance object associated with the OwnerDetails and save it
        insurance = Insurance(
            uuid=owner_details,
            insurance_id=insurance_id,
            coverage_type=coverage_type,
            start_date=start_date,
            end_date=end_date,
            insurance_coverage_amount=insurance_coverage_amount
        )
        insurance.save()

        # Redirect to a success page or do any other desired actions
        return redirect('user')  # Replace 'user' with your success page URL

    return render(request, 'insurance.html')

    



def logout_view(request):
    # Use Django's built-in logout function to log out the user
    logout(request)
    # Redirect to the homepage or any other desired page
    return redirect('login')  # Replace 'home' with the name of the URL pattern for your homepage
