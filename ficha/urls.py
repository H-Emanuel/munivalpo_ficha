from django.urls import path
from . import views

urlpatterns = [
    path('', views.ficha_home, name="ficha_home"),
    path('crear_ficha/', views.crear_ficha, name="crear_ficha"),
    path('editar_ficha/<int:id>', views.editar_ficha, name="editar_ficha"),
    path('ver_fichas/', views.ver_fichas, name="ver_fichas"),
    path('ver_ficha/<int:id>', views.ver_ficha, name="ver_ficha"),
    path('exportar_pdf/<int:id>', views.exportar_pdf, name="exportar_pdf"),
]