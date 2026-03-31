from django.contrib import admin
from django.urls import path, include
from post import views # Импортируем views из твоего приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/', include('post.urls')),
    
    # Теперь по пустому адресу открывается наша главная, а не редирект
    path('', views.index, name='index'), 
]