from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls' , namespace='accounts')),
    path('', include('courses.urls')),
    path('davomat/',include('davomat.urls')),
                #   path('contact/',include('contact.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
