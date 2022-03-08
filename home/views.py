from tkinter.messagebox import RETRY
from django.shortcuts import redirect, render
from .models import cashFlow

# Create your views here.
def index(request):
    cashflows = cashFlow.objects.all()
    return render(request, 'index.html', {'cashflows': cashflows})


def tambahCashflow(request):
    if request.method == 'POST':
        tanggal = request.POST['tanggal']
        keterangan = request.POST['keterangan']
        kuantitas = request.POST['kuantitas']
        nominal	= request.POST['nominal']

        cashflow = cashFlow.objects.create(tanggal=tanggal, keterangan=keterangan, kuantitas=kuantitas, nominal=nominal)
        cashflow.save()
        return  redirect('/')

    else:
        return render(request, 'tambahcashflow.html')

def hapusCashFlow(request, pk):
    if cashFlow.objects.filter(id=pk).exists():
         cashFlow.objects.filter(id=pk).delete()
         return redirect('/')

    else:
        return render(request, 'index.html')