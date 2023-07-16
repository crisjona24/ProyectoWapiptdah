"""
URL configuration for WAPIPTDAH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from APPWapiptdah.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #login 
    path('', login2, name='loginauthUser'), #Inicio de sesion
    path('validationUser/', validar, name='validationUser'),
    path('contacto/', contacto, name='contactanos'),
    #path('index/', prueba),
    #path('prueba/', prueba2),

    path('wapiptdah/', include('APPWapiptdah.urls')),

    #register
    #path('registrarCuenta/', formularioRegisterCuenta, name='registrar'),
    #path('guardarCuenta/', saveCuenta, name='guardarcuenta'),
    path('registrarActividad/', formularioRegisterActivity, name='registrarActividad'),

    # Usuario Comun
    path('registrarComun/', formularioRegisterComun, name='registrarUsuarioComun'),
    path('guardarComun/', saveUserComun, name='guardarUsuarioComun'),
    #path('editar_comun/<slug:slug>/', editarUsuarioComun, name='editar_comun'),
    #path('eliminar_usuariocomun/<slug:slug>/', eliminar_registro_usuariocomun, name='eliminar_usuariocomun'),
    #path('eliminar_usuariocomun_d/<slug:slug>/', eliminar_registro_usuariocomun_d, name='eliminar_usuariocomun_d'),

    # Usuario Tecnico
    path('registrarTecnico/', formularioRegisterTec, name='registrarUsuarioTecnico'),
    path('guardarTecnico/', saveUserTecnico, name='guardarUsuarioTecnico'),
    #path('editar_tecnico/<slug:slug>/', editarUsuarioTecnico, name='editar_tecnico'),
    #path('eliminar_usuariotecnico/<slug:slug>/', eliminar_registro_usuariotecnico, name='eliminar_usuariotecnico'),
    #path('eliminar_usuariotecnico_d/<slug:slug>/', eliminar_registro_usuariotecnico_d, name='eliminar_usuariotecnico_d'),
    
    # Paciente
    path('registrarPaciente/', formularioRegisterPaciente, name='registrarUsuarioPaciente'),
    path('guardarPaciente/', saveUserPaciente, name='guardarUsuarioPaciente'),
    #path('editar_paciente/<slug:slug>/', editarPaciente, name='editar_paciente'),
    #path('eliminar_paciente/<slug:slug>/', eliminar_registro_paciente, name='eliminar_paciente'),
    #path('eliminar_paciente_d/<slug:slug>/', eliminar_registro_paciente_d, name='eliminar_paciente_d'),

    # Perfiles
    #path('profile_user_paciente/', profile_user_paciente, name='profile_paciente'),
    #path('profile_user_comun/', profile_user_comun, name='profile_comun'),
    #path('profile_user_tecnico/', profile_user_tecnico, name='profile_tecnico'),

    # ventana principal
    path('homePaciente/', homePaciente, name='ventanaPrincipalPaciente'),
    path('homeTecnico/', homeTecnico, name='ventanaPrincipalTecnico'),
    path('homeComun/', homeComun, name='ventanaPrincipalComun'),

    # Listados

    # Listado de nivel de TDAH
    #path('listado_nivelTDAH_comun/', home_listado_nivelTDAH, name='listado_nivel_TDAH_c'),
    #path('listado_nivelTDAH_tecnico/<str:slug>/', home_listado_nivelTDAH_t, name='listado_nivel_TDAH_t'),
    #path('listado_nivelTDAH_paciente/', home_listado_nivelTDAH_p, name='listado_nivel_TDAH_p'),

    #Listado de categorias
    #path('listado_categoria_tecnico/', home_listado_categoria_t, name='listado_categoria_t'),
    #path('listado_categoria_comun/', home_listado_categoria_c, name='listado_categoria_c'),
    #path('listado_categoria_paciente/', home_listado_categoria_p, name='listado_categoria_p'),
    
    # Registros varios
    # Nivel de TDAH
    #path('registrarnivelTDAH/<str:slug>/', formularioRegisterNivelTDAH, name='registrar_de_NivelTDAH'),
    #path('guardarNivelTDAH/<str:slug>/', saveNivelTDAH, name='guardar_de_nivelTDAH'),
    #path('editar_GradoTDAH/<int:gradoTDAH_id>/', editar_GradoTDAH, name='editar_GradoTDAH'),
    #path('eliminar_GradoTDAH/<int:gradoTDAH_id>/', eliminar_registro_TDAH, name='eliminar_GradoTDAH'),
    #path('eliminar_GradoTDAH_d/<int:gradoTDAH_id>/', eliminar_registro_TDAH_d, name='eliminar_GradoTDAH_d'),

    # Curso
    #path('registrarCurso/', formularioRegisterCurso, name='registrar_de_Curso'),
    #path('guardarCurso/', saveCurso, name='guardar_de_Curso'),
    #path('editar_curso/<int:curso_id>/', editar_curso, name='editar_curso'),
    #path('eliminar_curso/<int:curso_id>/', eliminar_registro_curso, name='eliminar_curso'),
    #path('eliminar_curso_d/<int:curso_id>/', eliminar_registro_curso_d, name='eliminar_curso_d'),

    # Categoria
    #path('registrarCategoria/', formularioRegisterCategoria, name='registrar_de_Categoria'),
    #path('guardarCategoria/', saveCategoria, name='guardar_de_Categoria'),
    #path('editar_categoria/<int:categoria_id>/', editar_categoria, name='editar_categoria'),
    #path('eliminar_categoria/<int:categoria_id>/', eliminar_registro_categoria, name='eliminar_categoria'),
    #path('eliminar_categoria_d/<int:categoria_id>/', eliminar_registro_categoria_d, name='eliminar_categoria_d'),

    #Contenido
    #path('registrarContenido/', formularioRegisterContenido, name='registrar_de_Contenido'),
    #path('guardarContenido/', saveContenido, name='guardar_de_contenido'),
    #path('editar_contenido/<int:contenido_id>/', editar_contenido, name='editar_contenido'),
    #path('eliminar_contenido/<int:contenido_id>/', eliminar_registro_contenido, name='eliminar_contenido'),
    #path('eliminar_contenido_d/<int:contenido_id>/', eliminar_registro_contenido_d, name='eliminar_contenido_d'),

    #Resultados
    #path('registrarResultado/', formularioRegisterResultados, name='registrar_de_Resultado'),
    #path('guardarResultado/', saveResultado, name='guardar_de_resultados'),
    #path('editar_resultado/<int:resultado_id>/', editar_resultado, name='editar_resultado'),
    path('eliminar_resultado/<int:resultado_id>/', eliminar_registro_resultado, name='eliminar_resultado'),
    path('eliminar_resultado_d/<int:resultado_id>/', eliminar_registro_resultado_d, name='eliminar_resultado_d'),

    #Reportes
    #path('registrarReporte/', formularioRegisterReportes, name='registrar_de_Reportes'),
    #path('guardarReporte/', saveReporte, name='guardar_de_reportes'),
    #path('editar_reporte/<int:reporte_id>/', editar_reporte, name='editar_reporte'),

    #Sala
    #path('registrarSala/', formularioRegisterSala, name='registrar_de_Sala'),
    #path('guardarSala/', saveSala, name='guardar_de_sala'),
    #path('eliminar_sala/<int:sala_id>/', eliminar_registro_sala, name='eliminar_sala'),
    #path('eliminar_sala_d/<int:sala_id>/', eliminar_registro_sala_d, name='eliminar_sala_d'),

    #Peticion
    #path('registrarPeticion/', formularioRegisterPeticion, name='registrar_de_Peticion'),
    #path('guardarPeticion/', savePeticion, name='guardar_de_peticion'),
    #path('editar_peticion/<int:peticion_id>/', editar_peticion, name='editar_peticion'),
    #path('eliminar_peticion/<int:peticion_id>/', eliminar_registro_peticion, name='eliminar_peticion'),
    #path('eliminar_peticion_d/<int:peticion_id>/', eliminar_registro_peticion_d, name='eliminar_peticion_d'),

]
