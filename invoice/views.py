from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Invoice

class InvoiceListView(View):
    def get(self,*args,**kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request,'invoice/invoice-list.html',context)