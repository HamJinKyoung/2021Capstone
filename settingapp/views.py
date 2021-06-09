from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from main.models import Menu, CustomUser, Pay
from .forms import AddForm, EditForm, CustomForm
from datetime import datetime
from django.utils.dateformat import DateFormat

def setting(request):
    return render(request, 'settingapp/setting.html') 

def settingmenu(request):
    menus = Menu.objects.all()
    user = request.user
    return render(request, 'settingapp/settingmenu.html', {'menus': menus})

def addmenu(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.save()
            return redirect('settingmenu')
    else:
        form = AddForm()
        return render(request, 'settingapp/addmenu.html', {'form':form})

def editmenu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = EditForm(request.POST, instance=menu)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('settingmenu')
    else:
        form = EditForm(instance=menu)
        return render(request, 'settingapp/editmenu.html', {'form':form})

def delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('settingmenu')

def delete_user(request):
    request.user.delete()
    return redirect('home')
