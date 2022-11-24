from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('courses/', courses_view),
    path('courses/<slug:slug>', courses_detail),
    path('aply/', aply),
    
]
