# ===================================
# URLS DE LA API - libros/api_urls.py
# ===================================

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# 1. Importar tus vistas personalizadas
from .jwt_views import CustomTokenObtainPairView

# 2. Importar vistas de soporte de SimpleJWT
from rest_framework_simplejwt.views import (
    TokenRefreshView,           # Vista para refrescar access token
    TokenVerifyView,            # Vista para verificar token
)

# Importar ViewSets
from . import api_views

# ===== ROUTER PARA VIEWSETS =====
router = DefaultRouter()
router.register(r'libros', api_views.LibroViewSet, basename='libro')
router.register(r'autores', api_views.AutorViewSet, basename='autor')
router.register(r'categorias', api_views.CategoriaViewSet, basename='categoria')
router.register(r'prestamos', api_views.PrestamoViewSet, basename='prestamo')

# ===== URL PATTERNS =====
urlpatterns = [
    # ─────────────────────────────────
    # 🔐 AUTENTICACIÓN JWT (PERSONALIZADA)
    # ─────────────────────────────────
    
    # IMPORTANTE: Usamos CustomTokenObtainPairView en lugar de TokenObtainPairView
    path('auth/jwt/login/', CustomTokenObtainPairView.as_view(), name='jwt_login'),
    
    # Estas se mantienen igual
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # ─────────────────────────────────
    # 📚 ENDPOINTS DE LA API (CRUD)
    # ─────────────────────────────────
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import api_views
from . import oauth_views  # ← AGREGAR

router = DefaultRouter()
router.register(r'libros', api_views.LibroViewSet, basename='libro')
router.register(r'autores', api_views.AutorViewSet, basename='autor')
router.register(r'categorias', api_views.CategoriaViewSet, basename='categoria')
router.register(r'prestamos', api_views.PrestamoViewSet, basename='prestamo')

urlpatterns = [
    # ─────────────────────────────────
    # 🔐 AUTENTICACIÓN JWT
    # ─────────────────────────────────
    path('auth/jwt/login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # ─────────────────────────────────
    # 🔑 AUTENTICACIÓN OAUTH 2.0 (GOOGLE)
    # ─────────────────────────────────
    path('auth/google/redirect/', oauth_views.google_oauth_redirect, name='google_redirect'),
    path('auth/google/callback/', oauth_views.google_oauth_callback, name='google_callback'),
    
    # ─────────────────────────────────
    # 📚 ENDPOINTS CRUD
    # ─────────────────────────────────
    path('', include(router.urls)),
]