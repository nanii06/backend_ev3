
from django.contrib import admin
from django.contrib.auth import views as vistas_autenticacion
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',vistas_autenticacion.LoginView.as_view(template_name='registracion/login.html'),name='login',),
    path('logout/', vistas_autenticacion.LogoutView.as_view(), name='logout'),
    path('', include('deportesApp.urlsApp')),
]
