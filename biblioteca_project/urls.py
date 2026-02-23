from django.contrib import admin
from django.urls import path, include
from libros import web_views  # Tus vistas para la interfaz de prueba

urlpatterns = [
    # 1. Administración
    path('admin/', admin.site.urls),
    
    # 2. Endpoints de la API (Aquí es donde usas Postman o Curl)
    path('api/', include('libros.api_urls')),
    
    # 3. Páginas Web de Prueba (Frontend simple en Django)
    path('', web_views.home, name='home'),
    path('oauth/login/', web_views.oauth_login, name='oauth_login'),
    path('login/jwt/', web_views.jwt_login_page, name='jwt_login_page'),
    
    # 4. RUTAS NECESARIAS PARA ALLAUTH (Indispensables para Google Login)
    # Esto habilita /accounts/google/login/ y los callbacks
    path('accounts/', include('allauth.urls')),
]