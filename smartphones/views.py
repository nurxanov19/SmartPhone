from django.shortcuts import render
from .models import SmartPhone

def home(request):
    return render(request, 'home.html')

def phone_list(request):
    phones = SmartPhone.objects.all()
    context = {'phones': phones}
    return render(request, 'home.html', context=context)


def phone_detail(request, pk):
    phones = SmartPhone.objects.get(id = pk)
    context = {'phones': phones}
    return render(request, 'phone_detail', context=context)
