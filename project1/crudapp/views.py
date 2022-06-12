from pickle import OBJ
from django.shortcuts import render, redirect
from .forms import LaptopForm
from .models import Laptop
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
@login_required(login_url='login_url')
def Laptop_View(request):
    form = LaptopForm()
    template_name = 'crudapp/laptopform.html'
    
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlaptop_url')
    context = {'form': form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def Showlaptop_View(request, page=1):
    data = Laptop.objects.all()
    template_name ='crudapp/showlaptop.html'
    paginator = Paginator(data, 2)
    
    try:
        obj = paginator.page(page)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
        
    context = {'obj' : obj}
    return render(request, template_name, context)

def Update_View(request, id):
    data = Laptop.objects.get(laptop_id = id)
    form = LaptopForm(instance=data)
    template_name = 'crudapp/laptopform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=data)
        form.is_valiod()
        form.save()
        return redirect('showlaptop_url')
    return render(request, template_name, context)
def Delete_View(request, id):
    data = Laptop.objects.get(laptop_id = id)
    template_name = 'crudapp/confirmation.html'
    context = {'obj':data}
    if request.method == 'POST':
        data.delete()
        return redirect('showlaptop_url')
    return render(request, template_name, context)
    
