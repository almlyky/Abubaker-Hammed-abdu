from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your views here.

class Products(TemplateView):
    template_name='home.html'


def index(request):
    # Product.objects.all()  select all data
    # Product.objects.all()[0]  select one data
    # Product.objects.get(pk=1)  select one data with id
    return render(request,'home.html',{'data':Product.objects.all()})

def create(request):
    # Product.objects.create(pr_name="nokia",pr_price=300000)
    p1=Product(pr_name='samsong',pr_price=1300)
    p1.save()
    return HttpResponse(" تم الاضافه بنجاح")
def delete(request):
    p3=Product.objects.get(pk=1)
    p3.delete()
    return render(request,'home.html',{'data':Product.objects.all()})
