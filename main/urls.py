from django.contrib import admin
from django.urls import path, include
from main.views import principal, mostrar_perfil
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='login'),
    path('admin/', admin.site.urls),
    path('principal/', principal, name='principal'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('contratos/', include('contratos.urls')),
    path('cargos/', include('cargos.urls')),
    path('personas/', include('personas.urls')),
    path('sstpersonas/', include('sstpersonas.urls')),
    path('sstempresa/', include('sstempresa.urls')),
    path('logout/', views.logout_usuario, name='logout'),
    path('admin/logout/', auth_views.LogoutView.as_view(template_name='admin_logout.html'), name='admin_logout'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
