latitude = request.POST.get('latitude')
longitude = request.POST.get('longitude')

Complaint.objects.create(
    user=request.user,
    location=request.POST['location'],
    description=request.POST['description'],
    latitude=latitude,
    longitude=longitude
)