from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, ElectricityBill
from .forms import ElectricityBillForm

def bill_list(request):
    bills = ElectricityBill.objects.all()
    return render(request, 'myapp/bill_list.html', {'bills': bills})

def bill_create(request):
    if request.method == 'POST':
        form = ElectricityBillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = ElectricityBillForm()
    return render(request, 'myapp/bill_form.html', {'form': form})

def bill_update(request, pk):
    bill = get_object_or_404(ElectricityBill, pk=pk)
    if request.method == 'POST':
        form = ElectricityBillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('bill_list')
    else:
        form = ElectricityBillForm(instance=bill)
    return render(request, 'myapp/bill_form.html', {'form': form})

def bill_delete(request, pk):
    bill = get_object_or_404(ElectricityBill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'myapp/bill_confirm_delete.html', {'bill': bill})
