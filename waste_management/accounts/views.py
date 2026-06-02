from django.shortcuts import render
from wastebins.models import WasteBin
from complaints.models import Complaint
from accounts.models import User

def customer_dashboard(request):
    return render(request, 'citizen/dashboard.html')

def map_view(request):

    complaints = Complaint.objects.all()

    return render(
        request,
        'map.html',
        {'complaints': complaints}
    )

def my_complaints(request):
    return render(request, 'citizen/my_complaints.html')

# PASTE THIS BELOW THE OTHER FUNCTIONS

def admin_dashboard(request):

    total_bins = WasteBin.objects.count()

    total_complaints = Complaint.objects.count()

    total_drivers = User.objects.filter(
        role='Driver'
    ).count()

    context = {
        'total_bins': total_bins,
        'total_complaints': total_complaints,
        'total_drivers': total_drivers,
    }

    return render(
        request,
        'adminpanel/dashboard.html',
        context
    )
def complaint_form(request):
    return render(request, 'citizen/complaint_form.html')