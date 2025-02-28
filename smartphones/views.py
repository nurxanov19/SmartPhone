from django.shortcuts import render, redirect, get_object_or_404
from .models import SmartPhone

def home(request):
    return render(request, 'home.html')

def phone_list(request):
    phones = SmartPhone.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/phone_list.html', context=context)


def phone_detail(request, pk):
    phone = SmartPhone.objects.get(id = pk)
    context = {'phone': phone}
    return render(request, 'phones/phone_detail.html', context=context)


def create_phone(request):

    if request.method == 'POST':
        phone = SmartPhone()
        phone.brand = request.POST.get('brand', '')
        phone.model = request.POST.get('model', '')
        phone.country = request.POST.get('year', '')
        phone.color = request.POST.get('color', '')
        phone.year = request.POST.get('year', 0)
        phone.price = request.POST.get('price', 0)
        phone.description = request.POST.get('description', '')
        phone.image = request.FILES.get('image')
        print(phone.brand)
        phone.save()

        return redirect('phone-list')
    return render(request, 'phones/phone_create.html', {'phone': 'phone'})


def create_phone2(request):

    if request.method == 'POST':

        brand = request.POST['brand']
        model = request.POST['model']
        country = request.POST['country']
        color =request.POST['color']
        year = request.POST['year']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        SmartPhone.objects.create(
            brand=brand,
            model=model,
            country=country,
            color=color,
            year=year,
            price=price,
            description = description,
            image=image
        )
        return redirect('car-list')
    return render(request, 'phones/phone_create.html', {'phone':'phone'})

def update_phone(request, pk):
    phone = SmartPhone.objects.get(id=pk)
    if request.method == 'POST':
        phone.brand = request.POST.get('brand', phone.brand)
        phone.model = request.POST.get('model', phone.model)
        phone.country = request.POST.get('country', phone.country)
        phone.color = request.POST.get('color', phone.color)
        phone.year = request.POST.get('year', phone.year)
        phone.price = request.POST.get('price', phone.price)
        phone.description = request.POST.get('description', phone.description)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()

        return redirect('phone-detail', pk=phone.id)

    return render(request, 'phones/phone_update.html', {'phone': phone})


def delete_phone(request, pk):
    phone = get_object_or_404(SmartPhone, id =pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone-list')
    return render(request, 'phones/delete_phone.html', {'phone' : phone})

