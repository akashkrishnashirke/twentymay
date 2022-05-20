from django.shortcuts import render
from .models import mobiles_fiturs_model

# Create your views here.
def show(request):
    form= mobiles_fiturs_model.objects.all()
    md={'form':form}
    return render(request,'mobiles feature.html',context=md)