from clinics.models import Clinic
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'clinics/index.html', {'clinics': Clinic.objects.all()})
    #return HttpResponse('Hello clinics!')


def get_clinic(request, id):
    return render(request,'clinics/clinic.html',{'clinic': Clinic.objects.get(pk=id)})
