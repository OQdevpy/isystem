from dataclasses import fields
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.forms import modelformset_factory, inlineformset_factory
# Create your views here.


def davomat(request,pk):
    group=Group.objects.get(id=pk)

    context={
        'group':group,
    }
    return render(request,  'davomat/davomat.html',context)

def davomats(request):

    teacher = Teacher.objects.get(teacher=request.user)
    context={
        'teacher': teacher,
    }
    return render(request,  'davomat/davomat.html',context)
