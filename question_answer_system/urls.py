
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from qsapp import views


# main url paths
urlpatterns = [

    # admin panel endpoint
    path('admin/', admin.site.urls),

    # mapping to landing page localhost:8000
    url(r'^$', views.index, name="index"),

    # integreting the app url endpoints
    url(r'^qsapp/', include('qsapp.urls')),

]

# adding the staticfiles endpoints
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

