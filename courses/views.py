from django.shortcuts import redirect, render
from .models import *
from davomat.models import *
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context=None
    if request.user.id in Teacher.objects.all().values_list('id'):
        teacher=Teacher.objects.get(id=request.user.id)
        courses=teacher.course.all()
        context={
            'courses':courses,
        }
    return render(request,  'index.html',context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        contact=Contact()
        contact.name=request.POST.get('name')
        contact.email=request.POST.get('email')
        contact.msg=request.POST.get('msg')
        
        contact.save()
        return redirect(f'{request.get_full_path()}')
    return render(request, 'contact.html')


def courses_view(request):
    posts=Course.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'courses.html',context)


def courses_detail(request,slug):
    post=Course.objects.get(slug=slug)
    context={
        'post': post
             }
    return render(request, 'courses_detail.html',context)


def aply(request):
    posts=Course.objects.filter(is_published=True)
    if request.method == 'POST':
        aply=Aply()
        aply.name=request.POST.get('name')
        aply.age=request.POST.get('age')
        aply.phone=request.POST.get('phone')
        aply.q_phone=request.POST.get('q_phone')
        aply.kusr=request.POST.get('course')
        aply.save()
        return redirect("/")
    return render(request, 'apply.html',{"courses":posts})