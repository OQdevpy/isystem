from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls' , namespace='accounts')),
    path('', include('courses.urls')),
    path('davomat/',include('davomat.urls')),
                #   path('contact/',include('contact.urls')),
]
