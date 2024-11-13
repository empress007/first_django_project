from django.shortcuts import render
from . models import Profile
# Create your views here.
def profileHome(request):
    profile = Profile.objects.all().first()
    context = {
        # "name": "Ige Tolulope"
        "name": profile.name,
        "location": profile.address,
        # occupation,work_place
        # work_place = SQI College of ICT,Ibadan (ONLINE)
        "occupation": profile.occupation,
        "work_place": profile.work_place
        
    }
    return render(request, 'profile.html',context)