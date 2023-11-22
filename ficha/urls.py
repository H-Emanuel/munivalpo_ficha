from django.urls import path
from . import views

urlpatterns = [
    path('', views.ficha_home, name="ficha_home"),
    path('crear_ficha/', views.crear_ficha, name="crear_ficha"),
    path('editar_ficha/<int:id>', views.editar_ficha, name="editar_ficha"),
    path('ver_fichas/', views.ver_fichas, name="ver_fichas"),
    path('ver_ficha/<int:id>', views.ver_ficha, name="ver_ficha"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('exportar_pdf/<int:id>', views.exportar_pdf, name="exportar_pdf"),
    path('test_pdf/<int:id>', views.test_pdf, name="test_pdf"),
    path('get_location/', views.get_location, name="get_location"),
    path('actualizar_observacion/<int:id_plano>/', views.actualizar_observacion, name='actualizar_observacion'),
    path('actualizar_observacion_staff/<int:id_plano>/', views.actualizar_observacion_staff, name='actualizar_observacion_staff'),
    path('exportar_pdf_valoracion/<int:id>/', views.exportar_pdf_valoracion, name="exportar_pdf_valoracion"),
    path('guarda_observaciones/<int:id>/', views.guarda_observaciones, name="guarda_observaciones"),
    path('progresion/', views.progresion, name="progresion"),

]
