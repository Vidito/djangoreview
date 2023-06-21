from django.contrib import admin
from django.urls import path
from poems import views
from django.conf.urls.static import static
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('poems/<int:id>/', views.poem_detail, name='poem_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
