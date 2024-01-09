from django.shortcuts import render, redirect, get_object_or_404
from .models import CarBrand, CarModel, Collection, Owner
from .forms import CarBrandForm, CarModelForm, CollectionForm, OwnerForm

def home(request):
    car_models = CarModel.objects.all()[:3]
    return render(request, 'home.html', {'car_models': car_models})

def about(request):
    return render(request, 'about.html')

def collection_list(request):
    all_collections = Collection.objects.all()
    return render(request, 'collection_list.html', {'collections': all_collections})

def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'collection_detail.html', {'collection': collection})

def collection_create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_list')
    else:
        form = CollectionForm()

    return render(request, 'collection_form.html', {'form': form})

def collection_update(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)

    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_list')
    else:
        form = CollectionForm(instance=collection)

    return render(request, 'collection_form.html', {'form': form})

def collection_delete(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    
    if request.method == 'POST':
        collection.delete()
        return redirect('collection_list')

    return render(request, 'collection_confirm_delete.html', {'collection': collection})

def car_brand_list(request):
    car_brands = CarBrand.objects.all()
    return render(request, 'car_brand_list.html', {'car_brands': car_brands})

def car_brand_detail(request, pk):
    car_brand = get_object_or_404(CarBrand, pk=pk)
    return render(request, 'car_brand_detail.html', {'car_brand': car_brand})

def car_brand_create(request):
    if request.method == 'POST':
        form = CarBrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_brand_list')
    else:
        form = CarBrandForm()
    return render(request, 'car_brand_form.html', {'form': form})

def car_brand_update(request, pk):
    car_brand = get_object_or_404(CarBrand, pk=pk)
    if request.method == 'POST':
        form = CarBrandForm(request.POST, instance=car_brand)
        if form.is_valid():
            form.save()
            return redirect('car_brand_list')
    else:
        form = CarBrandForm(instance=car_brand)
    return render(request, 'car_brand_form.html', {'form': form})

def car_brand_delete(request, pk):
    car_brand = get_object_or_404(CarBrand, pk=pk)
    car_brand.delete()
    return redirect('car_brand_list')

def car_model_detail(request, brand_id, model_id):
    car_brand = get_object_or_404(CarBrand, pk=brand_id)
    car_model = get_object_or_404(CarModel, pk=model_id)
    return render(request, 'car_model_detail.html', {'car_brand': car_brand, 'car_model': car_model})

def car_model_create(request, brand_id):
    car_brand = get_object_or_404(CarBrand, pk=brand_id)
    
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            car_model = form.save(commit=False)
            car_model.brand = car_brand
            car_model.save()
            return redirect('car_brand_detail', pk=brand_id)
    else:
        form = CarModelForm()

    return render(request, 'car_model_form.html', {'car_brand': car_brand, 'form': form})

def car_model_update(request, brand_id, model_id):
    car_brand = get_object_or_404(CarBrand, pk=brand_id)
    car_model = get_object_or_404(CarModel, pk=model_id)

    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES, instance=car_model)
        if form.is_valid():
            form.save()
            return redirect('car_brand_detail', pk=brand_id)
    else:
        form = CarModelForm(instance=car_model)

    return render(request, 'car_model_form.html', {'car_brand': car_brand, 'form': form})

def car_model_delete(request, brand_id, model_id):
    car_brand = get_object_or_404(CarBrand, pk=brand_id)
    car_model = get_object_or_404(CarModel, pk=model_id)
    
    if request.method == 'POST':
        car_model.delete()
        return redirect('car_model_list', brand_id=brand_id)

    return render(request, 'car_model_confirm_delete.html', {'car_brand': car_brand, 'car_model': car_model})

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'owner_form.html', {'form': form, 'action': 'Create'})

def owner_update(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form, 'action': 'Update'})

def owner_delete(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list')
    return render(request, 'owner_confirm_delete.html', {'owner': owner})    