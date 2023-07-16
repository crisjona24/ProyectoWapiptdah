from django.urls import path
from . import views

urlpatterns = [

    # Perfiles de usuario
    path('paciente/profile_user_paciente/<str:slug>/', views.profile_user_paciente, name='profile_paciente'),
    path('comun/profile_user_comun/<str:slug>/', views.profile_user_comun, name='profile_comun'),
    path('tecnico/profile_user_tecnico/<str:slug>/', views.profile_user_tecnico, name='profile_tecnico'),

    # Listados de nivel de TDAH
    path('comun/listado_nivelTDAH_comun/<str:slug>/', views.home_listado_nivelTDAH, name='listado_nivel_TDAH_c'),
    path('comun/listado_nivelTDAH_comun_g/<str:slug1>/<str:slug2>/', views.home_listado_nivelTDAH_g, name='listado_nivel_TDAH_c_g'),
    path('tecnico/listado_nivelTDAH_tecnico/<str:slug>/', views.home_listado_nivelTDAH_t, name='listado_nivel_TDAH_t'),
    path('paciente/listado_nivelTDAH_paciente/<str:slug>/', views.home_listado_nivelTDAH_p, name='listado_nivel_TDAH_p'),
    
    # Registro de nivel de TDAH
    path('tecnico/registrarnivelTDAH/<str:slug>/', views.formularioRegisterNivelTDAH, name='registrar_de_NivelTDAH'),
    path('tecnico/guardarNivelTDAH/<str:slug>/', views.saveNivelTDAH, name='guardar_de_nivelTDAH'),
 
    # Listado de cursos
    path('comun/listado_cursos_comun/<str:slug>/', views.listado_cursos_c, name='listado_curso_c'),
    path('tecnico/listado_cursos_tecnico/<str:slug>/', views.listado_cursos_t, name='listado_curso_t'),
    path('paciente/listado_cursos_paciente/<str:slug>/', views.listado_cursos_p, name='listado_curso_p'),

    # Operaciones de cursos
    path('comun/registrarCurso/<str:slug>/', views.formularioRegisterCurso, name='registrar_de_Curso'),
    path('comun/guardarCurso/<str:slug>/', views.saveCurso, name='guardar_de_Curso'),
    path('comun/editar_curso/<str:slug>/', views.editar_curso, name='editar_curso'),
    path('comun/eliminar_curso_d/<str:slug>/', views.eliminar_registro_curso_d, name='eliminar_curso_d'),
    path('usuario/detalle_curso/<str:slug>/<str:slug2>/', views.detalle_curso_, name='detalle_de_curso'),

    # Listado de pacientes
    path('comun/listado_pacientes/<str:slug>/', views.listado_paciente_c, name='lista_de_pacientes_c'),
    path('tecnico/listado_pacientes/<str:slug>/', views.listado_paciente_t, name='lista_de_pacientes_t'),

    # Usuario Comun
    path('comun/editar_comun/<str:slug>/', views.editarUsuarioComun, name='editar_comun'),
    path('comun/eliminar_usuariocomun/<str:slug>/', views.eliminar_registro_usuariocomun, name='eliminar_usuariocomun'),
    path('comun/eliminar_usuariocomun_d/<str:slug>/', views.eliminar_registro_usuariocomun_d, name='eliminar_usuariocomun_d'),

    # Usuario Tecnico
    path('tecnico/editar_tecnico/<str:slug>/', views.editarUsuarioTecnico, name='editar_tecnico'),
    path('tecnico/eliminar_usuariotecnico/<str:slug>/', views.eliminar_registro_usuariotecnico, name='eliminar_usuariotecnico'),
    path('tecnico/eliminar_usuariotecnico_d/<str:slug>/', views.eliminar_registro_usuariotecnico_d, name='eliminar_usuariotecnico_d'),

    # Usuario Paciente
    path('paciente/editar_paciente/<str:slug>/', views.editarPaciente, name='editar_paciente'),
    path('paciente/eliminar_paciente/<str:slug>/', views.eliminar_registro_paciente, name='eliminar_paciente'),
    path('paciente/eliminar_paciente_d/<str:slug>/', views.eliminar_registro_paciente_d, name='eliminar_paciente_d'),

    # Listado de categorias
    path('tecnico/listado_categoria_tecnico_g/<str:slug>/', views.home_listado_categoria_t_general, name='listado_categoria_t_general'),
    path('tecnico/listado_categoria_tecnico/<str:slug>/', views.home_listado_categoria_t, name='listado_categoria_t'),
    path('comun/listado_categoria_comun/<str:slug>/<str:slug2>/', views.home_listado_categoria_c, name='listado_categoria_c'),
    path('paciente/listado_categoria_paciente/<str:slug>/<str:slug2>/', views.home_listado_categoria_p, name='listado_categoria_p'),

    # Operaciones de Grado TDAH
    path('tecnico/editar_GradoTDAH/<str:slug>/', views.editar_GradoTDAH, name='editar_GradoTDAH'),
    path('tecnico/eliminar_GradoTDAH_d/<str:slug>/', views.eliminar_registro_TDAH_d, name='eliminar_GradoTDAH_d'),

    # Listado de Contenido
    path('tecnico/listado_contenido_tecnico/<str:slug>/', views.home_listado_contenido_t, name='listado_contenido_t'),
    path('comun/listado_contenido_comun/<str:slug>/<str:slug2>/', views.home_listado_contenido_c, name='listado_contenido_c'),
    path('paciente/listado_contenido_paciente/<str:slug>/<str:slug2>/', views.home_listado_contenido_p, name='listado_contenido_p'),

    # Operaciones de Categoria
    path('tecnico/registrarcategoria/<str:slug>/', views.formularioRegisterCategoria, name='registrar_de_Categoria'),
    path('tecnico/guardarCategoria/<str:slug>/', views.saveCategoria, name='guardar_de_Categoria'),
    path('tecnico/editar_categoria/<str:slug>/', views.editar_categoria, name='editar_categoria'),
    path('tecnico/eliminar_categoria_d/<str:slug>/', views.eliminar_registro_categoria_d, name='eliminar_categoria_d'),
    path('comun/detalle_categoria_c/<str:slug>/<str:slug2>/', views.detalle_categoria_c, name='detalle_de_categoria_c'),

    # Operaciones de contenido
    path('tecnico/registrarContenido/<str:slug>/', views.formularioRegisterContenido, name='registrar_de_Contenido'),
    path('tecnico/guardarContenido/<str:slug>/', views.saveContenido, name='guardar_de_contenido'),
    path('tecnico/editar_contenido/<str:slug>/', views.editar_contenido, name='editar_contenido'),
    path('tecnico/eliminar_contenido_d/<str:slug>/', views.eliminar_registro_contenido_d, name='eliminar_contenido_d'),
    path('comun/detalle_contenido_c/<str:slug>/<str:slug2>/', views.detalle_contenido_c, name='detalle_de_contenido_c'),

    # Listado de peticiones
    path('tecnico/listado_peticiones_tecnico/<str:slug>/', views.home_listado_peticiones_t, name='listado_peticiones_t'),
    path('comun/listado_peticiones_tecnico/<str:slug>/', views.home_listado_peticiones_c, name='listado_peticiones_c'),

    # Operaciones de peticiones
    path('comun/registrarPeticion/<str:slug>/', views.formularioRegisterPeticion, name='registrar_de_Peticion'),
    path('comun/guardarPeticion/<str:slug>/', views.savePeticion, name='guardar_de_peticion'),
    path('comun/editar_peticion/<str:slug>/', views.editar_peticion, name='editar_peticion'),
    path('comun/eliminar_peticion_d/<str:slug>/', views.eliminar_registro_peticion_d, name='eliminar_peticion_d'),
    path('usuario/detalle_peticion/<str:slug>/<str:slug2>/', views.detalle_peticion, name='detalle_de_peticion'),
    
    # Operaciones de salas
    path('tecnico/listado_sala_tecnico/<str:slug>/', views.home_listado_sala_t, name='listado_sala_t'),
    path('comun/listado_sala_comun/<str:slug>/', views.home_listado_sala_c, name='listado_sala_c'),
    path('comun/registrarSala/<str:slug>/', views.formularioRegisterSala, name='registrar_de_Sala'),
    path('comun/guardarSala/<str:slug>/', views.saveSala, name='guardar_de_sala'),
    path('comun/eliminar_sala_d/<str:slug>/', views.eliminar_registro_sala_d, name='eliminar_sala_d'),
    path('comun/editar_sala/<str:slug>/', views.editar_sala, name='editar_sala'),

    # Operaciones de reportes
    path('tecnico/listado_reportes_tecnico/<str:slug>/', views.home_listado_reportes_t, name='listado_reportes_t'),
    path('comun/listado_reportes_tecnico/<str:slug>/', views.home_listado_reportes_c, name='listado_reportes_c'),
    path('comun/registrarReporte/<str:slug1>/<str:slug2>/', views.formularioRegisterReportes, name='registrar_de_Reporte'),
    path('comun/guardarReporte/<str:slug1>/<str:slug2>/', views.saveReporte, name='guardar_de_reporte'),
    path('comun/editar_reporte/<str:slug>/', views.editar_reporte, name='editar_reporte'),
    path('usuario/detalle_reporte/<str:slug>/<str:slug2>/', views.ver_detalle_reporte_c, name='detalle_reporte_c'),

    # Operaciones de resultados
    path('tecnico/listado_resultados_tecnico/<str:slug>/', views.home_listado_resultados_t, name='listado_resultados_t'),
    path('comun/listado_resultados_tecnico/<str:slug>/', views.home_listado_resultados_c, name='listado_resultados_c'),
    path('paciente/registrarResultado/<str:slug1>/<str:slug2>/', views.formularioRegisterResultados, name='registrar_de_Resultado'),
    path('paciente/editar_resultado/<str:slug1>/<str:slug2>/', views.editar_resultado, name='editar_resultado'),
    path('usuario/detalle_resultado/<str:slug>/<str:slug2>/', views.ver_detalle_resultado, name='detalle_resultado'),

    # Detalles
    path('usuario/detalle_nivel/<str:slug>/<str:slug2>/', views.detalle_nivel, name='detalle_de_nivel'),
    path('usuario/detalle_sala/<str:slug>/<str:slug2>/', views.detalle_sala, name='detalle_de_sala'),

    # Registro en curso
    path('usuario/registro_en_curso/<str:slug>/<str:slug2>/', views.registrarseCurso, name='registro_en_curso'),


]