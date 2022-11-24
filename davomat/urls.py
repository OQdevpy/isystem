from django.urls import path
from .views import davomat,davomats

urlpatterns = [
      path('', davomats),
      path('<int:pk>', davomat)
      
      
]