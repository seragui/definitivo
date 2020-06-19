from django.urls import path
from apps.usuarios.views import *
from django.contrib.auth.decorators import login_required


urlpatterns =[
    path('listado_usuarios/',login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
    path('resgistrar_usuario/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario'),

]