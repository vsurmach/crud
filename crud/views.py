from django.shortcuts import render, redirect, get_object_or_404

from .forms import ModelNewCarForm, FormNewCarForm
from .models import Car, Concern, Showroom


def get_one(request):
    return render(request, 'hello.html')


# HTML форма

def new_car(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        engine = request.POST.get('engine')
        year = request.POST.get('year')
        color = request.POST.get('color')
        Car.objects.create(brand=brand, engine=engine, year=year, color=color)
        return redirect('crud:view_cars')
    return render(request, 'new_car.html')


def view_cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'view_cars.html', context)


def edit_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        car.brand = request.POST.get('brand')
        car.engine = request.POST.get('engine')
        car.year = request.POST.get('year')
        car.color = request.POST.get('color')
        car.save()
        return redirect('crud:view_cars')
    context = {'car': car}
    return render(request, 'edit_car.html', context)


def delete_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('crud:view_cars')
    return render(request, 'delete_car.html', {'car': car})


# ModelForm

def model_new_car(request):
    form = ModelNewCarForm()
    if request.method == 'POST':
        form = ModelNewCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:model_view')
    context = {'form': form}
    return render(request, 'modelform/model_new_car.html', context)


def model_view_cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'modelform/model_view_cars.html', context)


def model_edit_car(request, pk):
    car = get_object_or_404(Car, id=pk)
    form = ModelNewCarForm(instance=car)
    if request.method == 'POST':
        form = ModelNewCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('crud:model_view')
    context = {'form': form}
    return render(request, 'modelform/model_edit_car.html', context)


def model_delete_car(request, pk):
    car = get_object_or_404(Car, id=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('crud:model_view')
    return render(request, 'modelform/model_delete_car.html', {'car': car})


# #formsForm

def form_new_car(request):
    form = FormNewCarForm()
    if request.method == 'POST':
        form = FormNewCarForm(request.POST)
        if form.is_valid():
            car = Car.objects.create(brand=form.cleaned_data['brand'],
                                     engine=form.cleaned_data['engine'],
                                     year=form.cleaned_data['year'],
                                     color=form.cleaned_data['color'],
                                     concern_id=form.cleaned_data['concern'].id)
            for i in form.cleaned_data['showroom']:
                car.showroom.add(i)
            return redirect('crud:form_view')
    context = {'form': form}
    return render(request, 'formform/form_new_car.html', context)


def form_view_cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'formform/form_view_cars.html', context)


def form_edit_car(request, pk):
    car = get_object_or_404(Car, id=pk)
    table = {
        'brand': car.brand,
        'engine': car.engine,
        'year': car.year,
        'color': car.color,
        'concern': car.concern,
        'showroom': car.showroom.all
    }
    form = FormNewCarForm(initial=table)
    if request.method == 'POST':
        form = FormNewCarForm(request.POST, initial=table)
        if form.is_valid():
            car.brand = form.cleaned_data['brand']
            car.engine = form.cleaned_data['engine']
            car.year = form.cleaned_data['year']
            car.color = form.cleaned_data['color']
            car.concern_id = form.cleaned_data['concern'].id
            car.showroom.set(form.cleaned_data['showroom'])
            car.save()
            return redirect('crud:form_view')
    context = {'form': form}
    return render(request, 'formform/form_edit_car.html', context)


def form_delete_car(request, pk):
    car = get_object_or_404(Car, id=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('crud:form_view')
    return render(request, 'formform/form_delete_car.html', {'car': car})
