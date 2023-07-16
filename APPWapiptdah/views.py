from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
#from django.core.exceptions import ValidationError #
from django.db import IntegrityError, transaction
#from django.contrib.auth.models import User
from APPWapiptdah.models import *
from datetime import datetime, date
import random, re
from django.urls import reverse
from cryptography.fernet import Fernet
from django.core.exceptions import ObjectDoesNotExist
#Instalar pip install cryptography

# Generar una clave secreta
clave_secreta = Fernet.generate_key()
cipher_suite = Fernet(clave_secreta)

def encriptar(slug):
    # Convertir el slug a bytes
    slug_bytes = slug.encode('utf-8')
    # Encriptar el slug
    slug_encriptado = cipher_suite.encrypt(slug_bytes)
    # Devolver el slug encriptado como texto base64
    return slug_encriptado.decode('utf-8')

def desencriptar(slug_encriptado):
    # Convertir el slug encriptado a bytes
    slug_encriptado_bytes = slug_encriptado.encode('utf-8')
    # Desencriptar el slug
    slug_bytes = cipher_suite.decrypt(slug_encriptado_bytes)
    # Devolver el slug desencriptado como texto
    return slug_bytes.decode('utf-8')

# Create your views here.
def prueba(request):
    return render(request, 'base/index.html', {})
def prueba2(request):
    return render(request, 'base/base.html', {})

# Metodo que permite validar el usuario y clave para el inicio de sesion
def validar(request):
    usuario = request.POST.get("username")
    clave = request.POST.get("password")

    if usuario and clave:
        if UsuarioComun.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).exists():
            # Inicio de sesión exitoso para Usuario Comun
            usuario_comun = UsuarioComun.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).first()
            if usuario_comun:  
                messages.success(request, "¡Bienvenido a WAPIPTDAH como Usuario Común!")
                slug_comun = usuario_comun.slug  # Obtener el slug del objeto
                slug_encriptado_comun = encriptar(slug_comun)  # Encriptar el slug
                url_c = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug_encriptado_comun})  # Generar la URL con el slug como parámetro                
                return redirect(url_c)
            
        elif UsuarioTecnico.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).exists():
            # Inicio de sesión exitoso para Usuario Tecnico
            usuario_tecnico = UsuarioTecnico.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).first()
            if usuario_tecnico:  
                messages.success(request, "¡Bienvenido a WAPIPTDAH como Usuario Tecnico!")
                slug_dato = usuario_tecnico.slug  # Obtener el slug del objeto
                #url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug})  # Generar la URL con el slug como parámetro
                #return redirect('listado_nivel_TDAH_t', slug=slug)
                slug = encriptar(slug_dato)
                url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug})
                return redirect(url)
        
        elif Paciente.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).exists():
            # Inicio de sesión exitoso para Paciente
            usuario_paciente = Paciente.objects.filter(correo_electronico__iexact=usuario, password__iexact=clave).first()
            if usuario_paciente:  
                messages.success(request, "¡Bienvenido a WAPIPTDAH como Paciente!")
                #slug_comun = usuario_comun.slug  # Obtener el slug del objeto
                #url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug_comun})  # Generar la URL con el slug como parámetro
                slug_paciente = usuario_paciente.slug  # Obtener el slug del objeto
                slug_encriptado_paciente = encriptar(slug_paciente)  # Encriptar el slug
                # Buscamos si el usuario esta registrado en un curso
                try:
                    detalle = DetallePacienteCurso.objects.get(paciente=usuario_paciente)
                    if detalle:
                        # El usuario esta registrado en un curso
                        url = reverse('listado_nivel_TDAH_p', kwargs={'slug': slug_encriptado_paciente})
                        return redirect(url)
                        
                except ObjectDoesNotExist:
                    # El usuario esta registrado en un curso
                    url = reverse('listado_curso_p', kwargs={'slug': slug_encriptado_paciente})
                    return redirect(url)    
        
        else:
            # Credenciales inválidas
            #messages.error(request, "Credenciales inválidas. Por favor, intente nuevamente.")
            #error_message = "Credenciales inválidas. Por favor, intente nuevamente."
            #return render(request, 'login/loginprueba.html', {'error': error_message})
            messages.error(request, "Por favor, ingrese su nombre de usuario y contraseña.")
            return redirect("/")
    else:
        # Campos de usuario y/o contraseña vacíos
        #error_message = "Por favor, ingrese su nombre de usuario y contraseña."
        #return render(request, 'login/loginprueba.html', {'error': error_message})
        messages.error(request, "Por favor, ingrese su nombre de usuario y contraseña.")
        return redirect("/")

# Renderizado de la pagina de login
def login2(request):
    return render(request, 'login/login_prueba.html', {})

# Renderizados de la pagina de contacto
@login_required
def contacto(request):
    return render(request, 'contacto/contacto.html', {})

#
#
#
#
## REGISTRO DE CUENTAS
#
#
#
# Renderizado del formulario de registro de Actividad
def formularioRegisterActivity(request):
   return render(request,'register/registerUser/register_Actividad.html', {})

# Validación de campos de registro: Clave 
def validate_user(data):
    #Se obtienen los datos del formulario
    password = data.get('password')
    confirm_password = data.get('password-confirm')
    email = data.get('email')

    #Se validan las claves que sean iguales
    if password != confirm_password:
        return "Las contraseñas no coinciden"
    #Se valida la presencias de todos los datos
    if any(value == '' for value in data.values()):
        return "Todos los campos son requeridos"
    #Se valida el tamaño de a clave ingresada 
    if len(password) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    #Se valida el formato de clave
    if not re.search(r'\d', password) or not re.search(r'[A-Z]', password):
        return "La contraseña debe tener al menos un número y una letra mayúscula"
    #Se determina un dominio especifico para el correo
    if not email.endswith('@unl.edu.ec'):
        return "El correo electrónico debe ser de dominio unl.edu.ec"

    return None
'''    
def formularioRegisterCuenta(request):
    return render(request, 'register/register/registrarCuentaPersonal.html', {})

def saveCuenta(request):
    data = request.POST
    validation_error = validate_user(data)
    if validation_error:
        return render(request, 'register/register/registrarCuentaPersonal.html', {'error': validation_error})
    try:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            email = request.POST.get('email')
            celular = request.POST.get('celular')
            direccion = request.POST.get('direccion')
            username = request.POST.get('username')
            password = request.POST.get('password')
            fecha = request.POST.get('fecha')

        user = Persona.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=email,
            numero_celular=celular,
            direccion=direccion,
            username=username,
            password=password,
            fecha_nacimiento=fecha,
            actividad = "UsuarioComun"
        )
        user.save() # Se guarda el usuario creado
        print("El usuario se guardo")
        return redirect('loginauthUser')
    except IntegrityError:
        error_message = "Usuario ya existe"
        return render(request, 'register/registerUser/registrarCuentaPersonal.html', {'error': error_message})
'''

# Renderizado del formulario de registro de Usuario Comun 
def formularioRegisterComun(request):
    return render(request,'register/registerUser/register_User_Comun.html', {})

#Metodo para guardar los datos de Usuario Comun 
def saveUserComun(request):
    data = request.POST
    validation_error = validate_user(data)
    #Se comprueba los errores posibles segun el método
    if validation_error:
        return render(request, 'register/registerUser/register_User_Comun.html', {'error': validation_error})
    try:
        #Se obtienen los datos de POST y se crea un objeto de modelo
        if request.method == 'POST':
            datos = request.POST
            nombre = datos.get('nombre')
            apellido = datos.get('apellido')
            email = datos.get('email')
            celular = datos.get('celular')
            genero = datos.get('genero')
            area_estudio = datos.get('area')
            username = datos.get('username')
            password = datos.get('password')
            fecha = datos.get('fecha')
        
        #Se comprueba la existencia única del correo electrónico
        if UsuarioComun.objects.filter(correo_electronico=email).exists() or \
           UsuarioTecnico.objects.filter(correo_electronico=email).exists() or \
           Paciente.objects.filter(correo_electronico=email).exists():
            error_message = "Usuario ya existe"
            return render(request, 'register/registerUser/register_User_Comun.html', {'error': error_message})

        usercomun = UsuarioComun.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=email,
            numero_celular=celular,
            genero = genero,
            area_estudio = area_estudio,
            username=username,
            password=password,
            fecha_nacimiento=fecha,
            actividad = "UsuarioComun"
        )
        usercomun.save() # Se guarda el usuario creado
        print("El usuario se guardo")
        return redirect('loginauthUser')
    except IntegrityError:
        error_message = "Usuario ya existe"
        return render(request, 'register/registerUser/register_User_Comun.html', {'error': error_message})

# Renderizado del formulario de registro de Usuario Técnico 
def formularioRegisterTec(request):
    return render(request,'register/registerUser/register_User_Tecnico.html', {})

#Metodo para guardar los datos de Usuario Técnico 
def saveUserTecnico(request):
    datos = request.POST
    validation_error = validate_user(datos)
    #Se comprueba los errores posibles segun el método
    if validation_error:
        return render(request, 'register/registerUser/register_User_Tecnico.html', {'error': validation_error})
    try:
        if request.method == 'POST':
            data = request.POST
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            celular = data.get('celular')
            identificacion = data.get('identificación')
            area_operacion = data.get('area')
            username = data.get('username')
            password = data.get('password')
            fecha = data.get('fecha')

        #Se comprueba la existencia única del correo electrónico
        if UsuarioComun.objects.filter(correo_electronico=email).exists() or \
           UsuarioTecnico.objects.filter(correo_electronico=email).exists() or \
           Paciente.objects.filter(correo_electronico=email).exists():
            error_message = "Usuario ya existe"
            return render(request, 'register/registerUser/register_User_Tecnico.html', {'error': error_message})

        usertec = UsuarioTecnico.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=email,
            numero_celular=celular,
            identificacion = identificacion,
            area_operacion = area_operacion,
            username=username,
            password=password,
            fecha_nacimiento=fecha,
            actividad = "UsuarioTecnico"
        )
        usertec.save() # Se guarda el usuario creado
        print("El usuario se guardo")
        return redirect('loginauthUser')
    except IntegrityError:
        error_message = "Usuario ya existe"
        return render(request, 'register/registerUser/register_User_Tecnico.html', {'error': error_message})

# Renderizado del formulario de registro de Paciente
def formularioRegisterPaciente(request):
    return render(request,'register/registerUser/register_User_Paciente.html', {})

#Método que permite calcular la edad a partir de un campo fecha
def calcular_edad(fecha_nacimiento):
    today = date.today()
    age = today.year - fecha_nacimiento.year
    # Verifica si el cumpleaños de este año ya ha pasado, si no, resta 1 a la edad
    if (
        today.month < fecha_nacimiento.month
        or (today.month == fecha_nacimiento.month and today.day < fecha_nacimiento.day)
    ):
        age -= 1
    return age

#Metodo para guardar los datos de Usuario Técnico 
def saveUserPaciente(request):
    datos = request.POST
    validation_error = validate_user(datos)
    #Se comprueba los errores posibles segun el método
    if validation_error:
        return render(request, 'register/registerUser/register_User_Paciente.html', {'error': validation_error})
    try:
        if request.method == 'POST':
            data = request.POST
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            celular = data.get('celular')
            contacto_emergencia = data.get('contacto')
            username = data.get('username')
            password = data.get('password')
            fecha = data.get('fecha')
            fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d').date()
            edad = calcular_edad(fecha_nacimiento)

        #Se comprueba la existencia única del correo electrónico
        if UsuarioComun.objects.filter(correo_electronico=email).exists() or \
           UsuarioTecnico.objects.filter(correo_electronico=email).exists() or \
           Paciente.objects.filter(correo_electronico=email).exists():
            error_message = "Usuario ya existe"
            return render(request, 'register/registerUser/register_User_Paciente.html', {'error': error_message})

        userpaciente = Paciente.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=email,
            numero_celular=celular,
            contacto_emergencia = contacto_emergencia,
            edad = edad,
            username=username,
            password=password,
            fecha_nacimiento=fecha_nacimiento,
            actividad = "Paciente"
        )
        userpaciente.save() # Se guarda el usuario creado
        print("El usuario se guardo")
        return redirect('loginauthUser')
    except IntegrityError:
        error_message = "Usuario ya existe"
        return render(request, 'register/registerUser/register_User_Paciente.html', {'error': error_message})



#
#
#
#
#
# REGISTROS
#
#
#
#
#


# GUARDAR REGISTRO DE TDAH

# Validación de campos completos
def validate_nivel(data):
    if any(value == '' for value in data.values()):
        return "Todos los campos son requeridos"
    return None

# Renderizado del formulario de registro de nivel de TDAH
def formularioRegisterNivelTDAH(request, slug):
    # Realizar la consulta al modelo GradoTDAH
    registros = GradoTDAH.objects.all()
    cantidad_registros = registros.count()

    # Verificar si existen solo dos registros
    if cantidad_registros == 2:
        # Manejar el caso en el que no hay exactamente dos registros
        nivelTDAH = GradoTDAH.objects.all()
        reporte = Reportes.objects.all()
        error_message = "Ya exsten dos niveles creados"
        return render(request, 'home_tecnico/listado_nivelTDAH_t.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug, 'error': error_message})
    
    else:
        return render(request, 'register/registerTDAH/register_NivelTDAH.html', {'slug': slug})

    
# Método para guardar la información del nivel
def saveNivelTDAH(request, slug):
    datos = request.POST
    slug = datos.get('slug')
    
    validation_error = validate_nivel(datos)
    #Se comprueba los errores posibles segun el método
    if validation_error:
        return render(request, 'register/registerTDAH/register_NivelTDAH.html', {'error': validation_error, 'slug':slug})
    try:
        if request.method == 'POST':
            data = request.POST
            nombre_nivel = data.get('nombre')
            numero_categorias = data.get('numcat')
            grado_dificultad = data.get('grado')
            descripcion_grado = data.get('descripcion')

            slug_desencriptado = desencriptar(data.get('slug'))
            tecnico = get_object_or_404(UsuarioTecnico, slug=slug_desencriptado)  # Obtener el objeto del técnico basado en el slug

        #Se comprueba la existencia del nivel
        if GradoTDAH.objects.filter(nombre_nivel=nombre_nivel).exists():
            error_message = "El nombre de nivel ya existe"
            return render(request, 'register/registerTDAH/register_NivelTDAH.html', {'error': error_message, 'slug':slug})

        nivelTDAH = GradoTDAH.objects.create(
            nombre_nivel=nombre_nivel,
            numero_categorias=numero_categorias,
            grado_dificultad=grado_dificultad,
            descripcion_grado=descripcion_grado,
            usuario_tecnico=tecnico
        )
        nivelTDAH.save() # Se guarda el usuario creado
        print("El nivel se guardo")
        return redirect('listado_nivel_TDAH_t', slug=slug)
    except IntegrityError:
        error_message = "Nivel ya existe"
        return render(request, 'register/registerTDAH/register_NivelTDAH.html', {'error': error_message, 'slug':slug})
    except GradoTDAH.DoesNotExist:
        error_message = "No existe el registro"
        # Manejar la excepción aquí, como redirigir a una página de error personalizada
        return render(request, 'error/404.html', {'error': error_message})

#GUARDAR REGISTRO DE CURSO

# Renderizado del formulario de registro de nivel de TDAH
def formularioRegisterCurso(request, slug):
    return render(request,'register/registerCurso/register_Curso.html', {'slug': slug})

# Método para guardar la información de curso
def saveCurso(request, slug):
    datos = request.POST
    slug = datos.get('slug') # Obtenemos el valor del slug

    validation_error = validate_nivel(datos)
    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerCurso/register_Curso.html', {'error': validation_error, 'slug': slug})
    try:
        if request.method == 'POST':
            data = request.POST
            nombre_curso = data.get('nombre')
            descripcion_curso = data.get('descripcion')

            # Desencriptamos el slug
            slug_desencriptado = desencriptar(slug)
            comun = get_object_or_404(UsuarioComun, slug=slug_desencriptado)  # Obtener el objeto del comun basado en el slug

        #Validación de la existencia única de un curso
        if Curso.objects.filter(nombre_curso=nombre_curso).exists():
            error_message = "El nombre de curso ya existe"
            return render(request, 'register/registerCurso/register_Curso.html', {'error': error_message, 'slug': slug})

        curso = Curso.objects.create(
            nombre_curso=nombre_curso,
            descripcion_curso=descripcion_curso,
            usuario_comun=comun
        )
        curso.save() # Se guarda el usuario creado
        print("El curso se guardo")
        return redirect('listado_nivel_TDAH_c', slug=slug)
    
    except IntegrityError:
        error_message = "Curso ya existe"
        return render(request, 'register/registerCurso/register_Curso.html', {'error': error_message, 'slug': slug})
    except Curso.DoesNotExist:
        error_message = "No existe el registro"
        # Manejar la excepción aquí, como redirigir a una página de error personalizada
        return render(request, 'error/404.html', {'error': error_message})

#GUARDAR REGISTRO DE CATEGORIA

# Renderizado del formulario de registro de categoría
def formularioRegisterCategoria(request, slug):
    return render(request,'register/registerCategoria/register_Categoria.html', {'slug': slug})

# Método para guardar la información de categoría
def saveCategoria(request, slug):
    datos = request.POST
    validation_error = validate_nivel(datos)

    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerCategoria/register_Categoria.html', {'error': validation_error, 'slug': slug})
    try:
        if request.method == 'POST':
            data = request.POST
            nombre_categoria = data.get('nombre')
            descripcion_categoria = data.get('descripcion')
            numtes = data.get('numtes')
            grado = data.get('grado')

        # Consulta para determinar la pertenencia a un nivel
        
        # Realizar la consulta utilizando join
        #grado_tdah = GradoTDAH.objects.select_related('usuario_tecnico').get(usuario_tecnico__slug=slug_t)
        # Obtener el slug del GradoTDAH
        #slug_grado_obtenido = grado_tdah.slug_grado

        # Obtener el objeto UsuarioTecnico por medio del slug
        ob_gradoTDAH = GradoTDAH.objects.get(slug_grado=slug)

        categoria = Categoria.objects.create(
            nombre_categoria=nombre_categoria,
            descripcion_categoria=descripcion_categoria,
            num_test = numtes,
            grado_dificultad = grado,
            grado_tdah_f = ob_gradoTDAH
        )
        categoria.save() # Se guarda el usuario creado
        print("La categoria se guardo")
        return redirect('listado_nivel_TDAH_t', slug=slug)
    
    except IntegrityError:
        error_message = "Categoria ya existe"
        return render(request, 'register/registerCategoria/register_Categoria.html', {'error': error_message, 'slug': slug})
    except Categoria.DoesNotExist:
        error_message = "No existe el registro"
        # Manejar la excepción aquí, como redirigir a una página de error personalizada
        return render(request, 'error/404.html', {'error': error_message})


#GUARDAR REGISTRO DE CONTENIDO

# Renderizado del formulario de registro de contenido
def formularioRegisterContenido(request, slug):
    return render(request,'register/registerContenido/register_Contenido.html', {'slug': slug})

# Método para guardar la información de contenido
def saveContenido(request, slug):
    datos = request.POST
    validation_error = validate_nivel(datos)
    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerContenido/register_Contenido.html', {'error': validation_error, 'slug': slug})
    try:
        if request.method == 'POST':
            data = request.POST
            nombrec = data.get('nombre')
            descripcionc = data.get('descripcion')
            contenidoc = data.get('contenido')
            dominioc = data.get('dominio')

        #Generación de un número random de cuatro dígitos que servirá como
        #identificativo
        codigoc = str(random.randint(1000, 9999))  # Generar un número de 4 dígitos

        # Obtener el objeto UsuarioTecnico por medio del slug
        ob_categoria = Categoria.objects.get(slug_categoria=slug)

        contenido = Contenido.objects.create(
            nombre=nombrec,
            descripcion=descripcionc,
            identificador_contenido = codigoc,
            contenido = contenidoc,
            dominio = dominioc,
            categoria = ob_categoria
        )
        contenido.save() # Se guarda el usuario creado

        print("El contenido se guardo")
        return redirect('listado_contenido_t', slug=slug)
        
    except IntegrityError:
        error_message = "Contenido ya existe"
        return render(request, 'register/registerContenido/register_Contenido.html', {'error': error_message, 'slug': slug})
    
    except Categoria.DoesNotExist:
        error_message = "Error al agregar"
        return render(request, 'error/404.html', {'error': error_message})

#GUARDAR REGISTRO DE RESULTADOS

# Renderizado del formulario de registro de resultados
def formularioRegisterResultados(request, slug1, slug2):
    # El slug recibido es de Paciente: el registra sus resultados por contenido
    return render(request,'register/registerResultados/register_Resultados.html', {'slug1': slug1, 'slug2': slug2})

# Método para guardar la información de resultados
def saveResultado(request, slug1, slug2):
    datos = request.POST
    validation_error = validate_nivel(datos)
    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerResultados/register_Resultados.html', {'error': validation_error})
    try:
        if request.method == 'POST':
            data = request.POST
            anotaciones = data.get('anotaciones')
            calificacion = data.get('calificacion')

        resultados = Resultados.objects.create(
            anotaciones=anotaciones,
            calificacion=calificacion
        )
        resultados.save() # Se guarda el usuario creado
        # Para redireccionar
        print("El resultado se guardo")
        return redirect('listado_nivel_TDAH_c', slug=slug1)
        #return redirect('ventanaPrincipalComun')
    except IntegrityError:
        error_message = "Resultado no se puede modificar"
        return render(request, 'register/registerResultados/register_Resultados.html', {'error': error_message})
    
#GUARDAR REGISTRO DE REPORTES

# Renderizado del formulario de registro de reporte
def formularioRegisterReportes(request, slug1, slug2):
    return render(request,'register/registerReportes/register_Reportes.html', {'slug1': slug1, 'slug2':slug2})

# Método para guardar la información de reporte
def saveReporte(request, slug1, slug2):

    # El slug cargado puede ser de paciente o de contenido
    datos = request.POST
    validation_error = validate_nivel(datos)
    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerReportes/register_Reportes.html', {'error': validation_error})
    try:
        if request.method == 'POST':
            data = request.POST
            titulo = data.get('titulo')
            descripcion = data.get('descripcion')

        # Obtnemos los objetos que se relacionan con el slug
        slug_des = desencriptar(slug2)
        ob_usarioC = UsuarioComun.objects.get(slug=slug_des)
        ob_contenido = Contenido.objects.get(slug_contenido=slug1)

        reporte = Reportes.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            usuario_comun = ob_usarioC,
            contenido_f = ob_contenido
        )
        reporte.save() # Se guarda el usuario creado

        # Reredireccionamos
        print("El reporte se guardo")
        slug_encriptado = encriptar(ob_usarioC.slug)
        return redirect('listado_nivel_TDAH_c', slug=slug_encriptado)

    except IntegrityError:
        error_message = "Reporte no se puede modificar"
        return render(request, 'register/registerReportes/register_Reportes.html', {'error': error_message})
    
#GUARDAR REGISTRO DE SALA

# Renderizado del formulario de registro de sala
def formularioRegisterSala(request, slug):
    return render(request,'register/registerSala/register_Sala.html', {'slug': slug})

# Método para guardar la información de sala
def saveSala(request, slug):
    if request.method == 'POST':
        datos = request.POST
        validation_error = validate_nivel(datos)

        # Busqueda de errores de campos vacios
        if validation_error:
            return render(request, 'register/registerSala/register_Sala.html', {'error': validation_error, 'slug': slug})

        try:
            data = request.POST
            indicaciones = data.get('indicaciones')

            with transaction.atomic():
                # Obtener el objeto UsuarioComun mediante el slug
                ob_usuariocomun = UsuarioComun.objects.get(slug=slug)

                sala = Sala.objects.create(
                    anotaciones=indicaciones,
                    usuario_comun=ob_usuariocomun
                )
                sala.save()  # Se guarda la sala creada

            print("La sala se guardó")
            return redirect('listado_nivel_TDAH_c', slug=slug)

        except IntegrityError:
            error_message = "No se puede crear la sala"
            return render(request, 'register/registerSala/register_Sala.html', {'error': error_message, 'slug': slug})
        
#GUARDAR REGISTRO DE PETICIÓN

# Renderizado del formulario de registro de petición
def formularioRegisterPeticion(request, slug):
    return render(request,'register/registerPeticion/register_Peticion.html', {'slug': slug})

# Método para guardar la información de petición
def savePeticion(request, slug):
    datos = request.POST
    validation_error = validate_nivel(datos)
    #Busqueda de errores de campos vacios
    if validation_error:
        return render(request, 'register/registerPeticion/register_Peticion.html', {'error': validation_error, 'slug': slug})
    try:
        if request.method == 'POST':
            data = request.POST
            motivo = data.get('motivo')
            peticion = data.get('peticion')
            tipo = data.get('tipo')

        # Obtener el objeto UsuarioTecnico por medio del slug
        ob_usuariocomun = UsuarioComun.objects.get(slug=slug)

        peticion = Peticion.objects.create(
            motivo_peticion=motivo,
            peticion = peticion,
            tipo_peticion = tipo,
            usuario_comun = ob_usuariocomun
        )
        peticion.save() # Se guarda el usuario creado

        print("La categoria se guardo")
        return redirect('listado_nivel_TDAH_c', slug=slug)
    
    except IntegrityError:
        error_message = "Petición no se puede crear"
        return render(request, 'register/registerPeticion/register_Peticion.html', {'error': error_message, 'slug': slug})

#
#
#
# EDICIONES
#
#
#

#EDICION DE CATEGORIA

def editar_categoria(request, slug):
    try:
        # El slug recibido es de CATEGORIA
        categoria = get_object_or_404(Categoria, slug_categoria=slug)

        if request.method == 'POST':
            # Validación de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Búsqueda de errores de campos vacíos
            if validation_error:
                return render(request, 'register/registerCategoria/edit_Categoria.html', {'categoria': categoria, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            numtes = request.POST['numtes']
            grado = request.POST['grado']

            # Actualizar los campos de la categoría existente
            categoria.nombre = nombre
            categoria.descripcion = descripcion
            categoria.numtes = numtes
            categoria.grado = grado
            categoria.save()

            # Redirigir a la página de detalles de la categoría actualizada
            url = reverse('listado_contenido_t', kwargs={'slug': slug})
            return redirect(url)

    except IntegrityError:
        error_message = "Categoria no se puede modificar"
        return render(request, 'register/registerCategoria/edit_Categoria.html', {'categoria': categoria, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404

    # Renderizar el formulario de edición con los datos existentes de la categoría
    return render(request, 'register/registerCategoria/edit_Categoria.html', {'categoria': categoria})


#EDICION DE PACIENTE

def editarPaciente(request, slug):
    try:
        slug_dp = desencriptar(slug)
        paciente = get_object_or_404(Paciente, slug=slug_dp)

        if request.method == 'POST':
            # Validación de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Búsqueda de errores de campos vacíos
            if validation_error:
                return render(request, 'register/registerUser/edit_User_Paciente.html', {'paciente': paciente, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            data = request.POST
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            celular = data.get('celular')
            contacto_emergencia = data.get('contacto')
            fecha = data.get('fecha')

            # Actualizar los campos del usuario paciente existente
            paciente.nombre = nombre
            paciente.apellido = apellido
            paciente.correo_electronico = email
            paciente.numero_celular = celular
            paciente.contacto_emergencia = contacto_emergencia
            paciente.fecha_nacimiento = fecha
            paciente.save()

            # Redirigir a la página de detalles del paciente actualizada
            #return redirect('registrarActividad')
            
            # Redirigir a la página de lista de niveles de tdah del paciente
            url = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug})
            return redirect(url)

    except IntegrityError:
        error_message = "Paciente no se puede modificar"
        return render(request, 'register/registerUser/edit_User_Paciente.html', {'paciente': paciente, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404

    # Renderizar el formulario de edición con los datos existentes del paciente
    return render(request, 'register/registerUser/edit_User_Paciente.html', {'paciente': paciente, 'slug': slug})

#EDICION DE USUARIO COMUN

def editarUsuarioComun(request, slug):
    try:
        slug_n = desencriptar(slug)
        comun = get_object_or_404(UsuarioComun, slug=slug_n)

        if request.method == 'POST':
            # Validación de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Búsqueda de errores de campos vacíos
            if validation_error:
                return render(request, 'register/registerUser/edit_User_Comun.html', {'comun': comun, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            celular = request.POST['celular']
            genero = request.POST['genero']
            area_estudio = request.POST['area']
            fecha = request.POST['fecha']

            # Actualizar los campos del usuario común existente
            comun.nombre = nombre
            comun.apellido = apellido
            comun.correo_electronico = email
            comun.numero_celular = celular
            comun.fecha_nacimiento = fecha
            comun.genero = genero
            comun.area_estudio = area_estudio
            comun.save()

            # Redirigir a la página de detalles del usuario común actualizado
            url_c = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug})  # Generar la URL con el slug como parámetro                
            return redirect(url_c)

    except IntegrityError:
        error_message = "Usuario no se puede modificar"
        return render(request, 'register/registerUser/edit_User_Comun.html', {'comun': comun, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404
    
    # Renderizar el formulario de edición con los datos existentes del usuario común
    return render(request, 'register/registerUser/edit_User_Comun.html', {'comun': comun, 'slug': slug})


#EDICION DE USUARIO TECNICO

def editarUsuarioTecnico(request, slug):
    try:
        slug_dt = desencriptar(slug)
        tecnico = get_object_or_404(UsuarioTecnico, slug=slug_dt) # Buscamos el registro

        if request.method == 'POST':
            # Validación de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Búsqueda de errores de campos vacíos
            if validation_error:
                return render(request, 'register/registerUser/edit_User_Tecnico.html', {'tecnico': tecnico, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            celular = request.POST['celular']
            area_operacion = request.POST['area']
            fecha = request.POST['fecha']

            # Actualizar los campos del usuario técnico existente
            tecnico.nombre = nombre
            tecnico.apellido = apellido
            tecnico.correo_electronico = email
            tecnico.numero_celular = celular,
            tecnico.fecha_nacimiento = fecha
            tecnico.area_operacion = area_operacion
            tecnico.save()
            
            # Redirigir a la página de detalles del usuario técnico actualizado

            url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug})
            return redirect(url)
            #return redirect('registrarActividad')

    except IntegrityError:
        error_message = "Usuario no se puede modificar"
        return render(request, 'register/registerUser/edit_User_Tecnico.html', {'tecnico': tecnico, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404

    # Renderizar el formulario de edición con los datos existentes del usuario técnico
    return render(request, 'register/registerUser/edit_User_Tecnico.html', {'tecnico': tecnico, 'slug': slug})


# EDICION DE CONTENIDO

def editar_contenido(request, slug):
    try:
        # el slug que llega es de CONTENIDO
        contenido = get_object_or_404(Contenido, slug_contenido=slug)
        # Encontramos el registro al que esta asociado el contenido
        ob_categoria = contenido.categoria

        if request.method == 'POST':
            datos = request.POST
            validation_error = validate_nivel(datos)

            if validation_error:
                return render(request, 'register/registerContenido/edit_Contenido.html', {'contenido': contenido, 'error': validation_error, 'slug': slug})

            data = request.POST
            nombrec = data.get('nombre')
            descripcionc = data.get('descripcion')
            contenidoc = data.get('contenido')
            dominioc = data.get('dominio')

            contenido.nombre = nombrec
            contenido.descripcion = descripcionc
            contenido.contenido = contenidoc  
            contenido.dominio = dominioc
            contenido.save()

            # Redirigir a la página de detalles de la categoría actualizada
            url = reverse('listado_contenido_t', kwargs={'slug': ob_categoria.slug_categoria})
            return redirect(url)

    except IntegrityError:
        error_message = "Contenido no se puede modificar"
        return render(request, 'register/registerContenido/edit_Contenido.html', {'contenido': contenido, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')

    return render(request, 'register/registerContenido/edit_Contenido.html', {'contenido': contenido, 'slug': slug})


# EDICION DE CURSO

def editar_curso(request, slug):
    try:   
        # El slug es del Curso
        curso = get_object_or_404(Curso, slug_curso=slug)
        # Validamos la existencia
        usuario_comun = curso.usuario_comun
        slug_usuario_comun = usuario_comun.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_comun)
        
        if request.method == 'POST':
            # Validación de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Búsqueda de errores de campos vacíos
            if validation_error:
                return render(request, 'register/registerCurso/edit_Curso.html', {'curso': curso, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            data = request.POST
            nombre_curso = data.get('nombre')
            descripcion_curso = data.get('descripcion')

            # Actualizar los campos del curso existente
            curso.nombre_curso = nombre_curso
            curso.descripcion_curso = descripcion_curso
            curso.save()

            url = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug_encriptado})
            return redirect(url)
            # Redirigir a la página de detalles del curso actualizado
            #return redirect('registrarCurso')

    except IntegrityError:
        error_message = "Curso no se puede modificar"
        return render(request, 'register/registerCurso/edit_Curso.html', {'curso': curso, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404

    # Renderizar el formulario de edición con los datos existentes del curso
    return render(request, 'register/registerCurso/edit_Curso.html', {'curso': curso, 'slug': slug})

# EDICION DE PETICION

def editar_peticion(request, slug):
    try:
        # Obtener la instancia de la peticion
        peticion = get_object_or_404(Peticion, slug_peticion=slug)

        if request.method == 'POST':
            data = request.POST
            validation_error = validate_nivel(data)

            if validation_error:
                return render(request, 'register/registerPeticion/edit_Peticion.html', {'peticion': peticion, 'error': validation_error, 'slug': slug})

            motivo = data.get('motivo')
            peticion_texto = data.get('peticion') 
            tipo = data.get('tipo')

            peticion.motivo_peticion = motivo
            peticion.peticion = peticion_texto 
            peticion.tipo_peticion = tipo
            peticion.save()

            slug_encriptado = encriptar(peticion.usuario_comun.slug)

            # Redireccionar a la lista de peticiones del usuario comun
            return redirect('listado_peticiones_c', slug=slug_encriptado)

    except IntegrityError:
        error_message = "La petición no se puede modificar"
        return render(request, 'register/registerPeticion/edit_Peticion.html', {'peticion': peticion, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')

    return render(request, 'register/registerPeticion/edit_Peticion.html', {'peticion': peticion, 'slug': slug})


# EDICION DE REPORTES

def editar_reporte(request, slug):
    try:
        reporte = get_object_or_404(Reportes, slug_reporte=slug)

        if request.method == 'POST':
            datos = request.POST
            validation_error = validate_nivel(datos) 

            if validation_error:
                return render(request, 'register/registerReportes/edit_Reporte.html', {'reporte': reporte, 'error': validation_error, 'slug': slug})

            data = request.POST
            titulo_text = data.get('titulo')
            descripcion_text = data.get('descripcion')

            reporte.titulo = titulo_text
            reporte.descripcion = descripcion_text
            reporte.save()
            
            # El slug del usuario comun y redireccionamos
            slug_encriptado = encriptar(reporte.usuario_comun.slug)

            # Redireccionar a la lista de peticiones del usuario comun
            return redirect('listado_nivel_TDAH_c', slug=slug_encriptado)

    except IntegrityError:
        error_message = "Reporte no se puede modificar"
        return render(request, 'register/registerReportes/edit_Reporte.html', {'reporte': reporte, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')

    return render(request, 'register/registerReportes/edit_Reporte.html', {'reporte': reporte, 'slug': slug})

# EDICION DE RESULTADOS

def editar_resultado(request, slug1, slug2):
    try:
        # El slug2 es propio del resultado
        resultado = get_object_or_404(Resultados, slug_resultado=slug2)

        if request.method == 'POST':
            datos = request.POST
            validation_error = validate_nivel(datos) 

            if validation_error:
                return render(request, 'register/registerResultados/register_Resultados.html', {'resultado': resultado, 'error': validation_error, 'slug1': slug1, 'slug2': slug2})

            data = request.POST
            anotaciones_ = data.get('anotaciones')
            calificacion_ = data.get('calificacion')

            resultado.anotaciones = anotaciones_
            resultado.calificacion = calificacion_
            resultado.save()

            # Redireccionar
            url = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug1})
            return redirect(url)

    except IntegrityError:
        error_message = "Resultado no se puede modificar"
        return render(request, 'register/registerResultados/register_Resultados.html', {'resultado': resultado, 'error': error_message, 'slug1': slug1, 'slug2': slug2})

    except Http404:
        return render(request, 'error/404.html')

    return render(request, 'register/registerResultados/register_Resultados.html', {'resultado': resultado, 'slug1': slug1, 'slug2': slug2})


# EDICION DE SALA

def editar_sala(request, slug):
    try:
        # El slug que llega es de sala
        sala = get_object_or_404(Sala, slug_sala=slug)

        if request.method == 'POST':
            datos = request.POST
            validation_error = validate_nivel(datos)  # Asegúrate de tener la implementación de la función validate_nivel

            if validation_error:
                return render(request, 'register/registerSala/edit_Sala.html', {'sala': sala, 'error': validation_error, 'slug': slug})

            data = request.POST
            indicaciones = data.get('indicaciones')

            sala.anotaciones = indicaciones

            # Encontramos el usuario comun asociado
            ob_ucomun = sala.usuario_comun
            # Obtenemos el slug del usuario
            slug_encriptado = encriptar(ob_ucomun.slug)
            # Editamos
            sala.save()

            url = reverse('listado_sala_c', kwargs={'slug': slug_encriptado})
            return redirect(url)

    except IntegrityError:
        error_message = "Sala no se puede modificar"
        return render(request, 'register/registerSala/edit_Sala.html', {'sala': sala, 'error': error_message})

    except Http404:
        return render(request, 'error/404.html')

    return render(request, 'register/registerSala/edit_Sala.html', {'sala': sala})

# EDICION DE NIVEL

def editar_GradoTDAH(request, slug):
    try:
        # buscamos si el slug pertenece a una categoria
        categoria_ob = Categoria.objects.get(slug_categoria=slug)
        # Buscamos el grado que se asocia a esa categoria
        grado_tdah_ob = categoria_ob.grado_tdah_f
        #Sacamos el slug del grado
        slug_grado = grado_tdah_ob.slug_grado # para editar
        # Validamos la existencia
        usuario_tecnico = grado_tdah_ob.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)

        if request.method == 'POST':
            # Validacion de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Busqueda de errores de campos vacios
            if validation_error:
                return render(request, 'register/registerTDAH/editar_GradoTDAH.html', {'grado': grado_tdah_ob, 'error': validation_error, 'slug': slug_grado})

            # Procesar los datos del formulario enviado
            data = request.POST
            nombre_text = data.get('nombre')
            numero_text = data.get('numcat')
            grado_text = data.get('grado')
            descripcion_ = data.get('descripcion')

            # Actualizar los campos del nivel existente
            grado_tdah_ob.nombre_nivel = nombre_text
            grado_tdah_ob.numero_categorias = numero_text
            grado_tdah_ob.grado_dificultad = grado_text
            grado_tdah_ob.descripcion_grado = descripcion_
            grado_tdah_ob.save()

            url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug_encriptado})
            return redirect(url)

    except Categoria.DoesNotExist:
        # El slug es del grado
        grado = get_object_or_404(GradoTDAH, slug_grado=slug)
        # Validamos la existencia
        usuario_tecnico = grado.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)
                
        if request.method == 'POST':
            # Validacion de errores
            datos = request.POST
            validation_error = validate_nivel(datos)

            # Busqueda de errores de campos vacios
            if validation_error:
                return render(request, 'register/registerTDAH/editar_GradoTDAH.html', {'grado': grado, 'error': validation_error, 'slug': slug})

            # Procesar los datos del formulario enviado
            data = request.POST
            nombre_text = data.get('nombre')
            numero_text = data.get('numcat')
            grado_text = data.get('grado')
            descripcion_ = data.get('descripcion')

            # Actualizar los campos del nivel existente
            grado.nombre_nivel = nombre_text
            grado.numero_categorias = numero_text
            grado.grado_dificultad = grado_text
            grado.descripcion_grado = descripcion_
            grado.save()

            url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug_encriptado})
            return redirect(url)

    except IntegrityError:
        error_message = "Grado TDAH no se puede modificar"
        return render(request, 'register/registerTDAH/editar_GradoTDAH.html', {'grado': grado, 'error': error_message, 'slug': slug})

    except Http404:
        return render(request, 'error/404.html')  # Renderizar una página personalizada de error 404

    # Renderizar el formulario de edición con los datos existentes de la sala
    return render(request, 'register/registerTDAH/editar_GradoTDAH.html', {'grado': grado, 'slug': slug})


    #
    #
    #
    #
    #
    # 
    # ELIMINACION
    #
    #
    #
    #
    #
    #

# ELIMINAR REGISTRO DE PACIENTE CON POST Y DIRECTO
def eliminar_registro_paciente(request, slug):
    try:
        slug_pPost = desencriptar(slug)
        registro = get_object_or_404(Paciente, slug=slug_pPost)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            #return redirect('lista_de_pacientes')

            # Redirigir a la página de login
            return redirect('loginauthUser')

    except Paciente.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_paciente_d(request, slug):
    try:
        slug_pd = desencriptar(slug)
        registro = get_object_or_404(Paciente, slug=slug_pd)
        # Eliminar el registro
        registro.delete()
        #return redirect('lista_de_pacientes')

        # Redirigir a la página de login
        return redirect('loginauthUser')

    except Paciente.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE USUARIO COMUM CON POST Y DIRECTO
def eliminar_registro_usuariocomun(request, slug):
    try:
        slug_d = desencriptar(slug) # Descifrado del slug
        registro = get_object_or_404(UsuarioComun, slug=slug_d)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            # Redirigir a la página de login
            return redirect('loginauthUser')
            #return redirect('lista_de_usuario_comun')

    except UsuarioComun.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_usuariocomun_d(request, slug):
    try:
        slug_DC = desencriptar(slug) # Descifrado del slug
        registro = get_object_or_404(UsuarioComun, slug=slug_DC)
        # Eliminar el registro
        registro.delete()
        # Redirigir a la página de login
        return redirect('loginauthUser')
        #return redirect('lista_de_usuario_comun')

    except Paciente.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})
    
    
# ELIMINAR REGISTRO DE USUARIO TECNICO CON POST Y DIRECTO
def eliminar_registro_usuariotecnico(request, slug):
    try:
        slug_tPost = desencriptar(slug) # Descifrado del slug
        registro = get_object_or_404(UsuarioTecnico, slug=slug_tPost)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            # Redirigir a la página de login
            return redirect('loginauthUser')
            #return redirect('lista_de_usuario_tecnico')

    except UsuarioTecnico.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_usuariotecnico_d(request, slug):
    try:
        slug_tDirect = desencriptar(slug) # Descifrado del slug
        registro = get_object_or_404(UsuarioTecnico, slug=slug_tDirect)
        # Eliminar el registro
        registro.delete()
        # Redirigir a la página de login
        return redirect('loginauthUser')

    except UsuarioTecnico.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE CATEGORIA CON POST Y DIRECTO
def eliminar_registro_categoria(request, categoria_id):
    try:
        registro = get_object_or_404(Categoria, id=categoria_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Categoria.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_categoria_d(request, slug):
    try:
        # buscamos si el slug pertenece a una categoria
        categoria_ob = Categoria.objects.get(slug_categoria=slug)
        # Buscamos el grado que se asocia a esa categoria
        grado_tdah_ob = categoria_ob.grado_tdah_f

        # Eliminar el registro
        categoria_ob.delete()

        # Redireccion
        url = reverse('listado_categoria_t', kwargs={'slug': grado_tdah_ob.slug_grado})
        return redirect(url)

    except Categoria.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE CONTENIDO CON POST Y DIRECTO
def eliminar_registro_contenido(request, contenido_id):
    try:
        registro = get_object_or_404(Contenido, id=contenido_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Contenido.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_contenido_d(request, slug):
    try:
        registro = get_object_or_404(Contenido, slug_contenido=slug)
        ob_categoria = registro.categoria
        # Eliminar el registro
        registro.delete()
        # Redireccionamos
        url = reverse('listado_contenido_t', kwargs={'slug': ob_categoria.slug_categoria})
        return redirect(url)

    except Contenido.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

# ELIMINAR REGISTRO DE CURSO CON POST Y DIRECTO
def eliminar_registro_curso(request, curso_id):
    try:
        registro = get_object_or_404(Curso, id=curso_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Curso.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_curso_d(request, slug):
    try:
        # El slug es del Curso
        curso = get_object_or_404(Curso, slug_curso=slug)
        # Validamos la existencia
        usuario_comun = curso.usuario_comun
        slug_usuario_comun = usuario_comun.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_comun)

        # Eliminar el registro
        curso.delete()

        url = reverse('listado_nivel_TDAH_c', kwargs={'slug': slug_encriptado})
        return redirect(url)

    except Curso.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE PETICION CON POST Y DIRECTO
def eliminar_registro_peticion(request, peticion_id):
    try:
        registro = get_object_or_404(Peticion, id=peticion_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Peticion.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_peticion_d(request, slug):
    try:
        # Obtener la peticion a eliminar
        peticion = get_object_or_404(Peticion, slug_peticion=slug)
        # Obtener el usuario comun asociado
        usuariocomun_ob = peticion.usuario_comun
        slug_encriptado = encriptar(usuariocomun_ob.slug)
        # Eliminar el registro
        peticion.delete()
        # Redireccionar a la lista de peticiones del usuario comun
        return redirect('listado_peticiones_c', slug=slug_encriptado)

    except Peticion.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro de la petición"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

# ELIMINAR REGISTRO DE RESULTADO CON POST Y DIRECTO
def eliminar_registro_resultado(request, resultado_id):
    try:
        registro = get_object_or_404(Resultados, id=resultado_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Resultados.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_resultado_d(request, resultado_id):
    try:
        registro = get_object_or_404(Resultados, id=resultado_id)
        # Eliminar el registro
        registro.delete()
        return redirect('registrarActividad')

    except Resultados.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE SALA CON POST Y DIRECTO
def eliminar_registro_sala(request, sala_id):
    try:
        registro = get_object_or_404(Sala, id=sala_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except Sala.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_sala_d(request, slug):
    try:
        # Obtener la peticion a eliminar
        sala_ob = get_object_or_404(Sala, slug_sala=slug)
        # Obtener el usuario comun asociado
        usuariocomun_ob = sala_ob.usuario_comun
        slug_encriptado = encriptar(usuariocomun_ob.slug)
        # Eliminar el registro
        sala_ob.delete()
        # Redireccionar a la lista de peticiones del usuario comun
        return redirect('listado_sala_c', slug=slug_encriptado)

    except Sala.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


# ELIMINAR REGISTRO DE SALA CON POST Y DIRECTO
def eliminar_registro_TDAH(request, gradoTDAH_id):
    try:
        registro = get_object_or_404(GradoTDAH, id=gradoTDAH_id)

        if request.method == 'POST':
            # Eliminar el registro
            registro.delete()
            return redirect('registrarActividad')

    except GradoTDAH.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})

def eliminar_registro_TDAH_d(request, slug):
    try:
        # buscamos si el slug pertenece a una categoria
        categoria_ob = Categoria.objects.get(slug_categoria=slug)
        # Buscamos el grado que se asocia a esa categoria
        grado_tdah_ob = categoria_ob.grado_tdah_f
        # Validamos la existencia
        usuario_tecnico = grado_tdah_ob.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)
        
        # Eliminar el registro
        grado_tdah_ob.delete()

        url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug_encriptado})
        return redirect(url)

    except Categoria.DoesNotExist:
        # El slug es del Curso
        registro = get_object_or_404(GradoTDAH, slug_grado=slug)
        # Validamos la existencia
        usuario_tecnico = registro.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)
        # Eliminar el registro
        registro.delete()

        url = reverse('listado_nivel_TDAH_t', kwargs={'slug': slug_encriptado})
        return redirect(url)

    except GradoTDAH.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

    except Exception as e:
        # Manejar cualquier otra excepción que pueda ocurrir
        error_message = str(e)
        return render(request, 'error/404.html', {'error': error_message})


#
#
#
#
#VENTANA PRINCIPAL
#
#
#
#
#

def homePaciente(request):
    return render(request, 'home_paciente/home_Paciente.html', {})

def homeTecnico(request):
    return render(request, 'home_tecnico/home_Tecnico.html', {})

def homeComun(request):
    return render(request, 'home_comun/home_Comun.html', {})


#
#
#
#
# LISTADOS
#
#
#
#
#

# Listado de Pacientes

def listado_paciente_c(request, slug):
    pacientes = Paciente.objects.all()
    return render(request, 'home_paciente/listado_paciente_c.html', {'paciente': pacientes, 'slug': slug})

def listado_paciente_t(request, slug):
    pacientes = Paciente.objects.all()
    return render(request, 'home_paciente/listado_paciente_t.html', {'paciente': pacientes, 'slug': slug})

# Listado de Niveles de TDAH

def home_listado_nivelTDAH(request, slug):
    try:
        slugt_d_lista = desencriptar(slug)
        usuario_ = get_object_or_404(UsuarioComun, slug=slugt_d_lista)
        nombre_usuario = usuario_.nombre
        # Obtenemos los datos necesarios
        nivelTDAH = GradoTDAH.objects.all()
        reporte = Reportes.objects.all()
        return render(request, 'home_comun/listado_nivelTDAH.html', {'nivelTDAH': nivelTDAH, 'usuario': nombre_usuario ,'reporte': reporte, 'slug': slug})

    except UsuarioComun.DoesNotExist:
        # Manejar el caso en que el registro no existe
        error_message = "No existe registro"
        return render(request, 'error/404.html', {'error': error_message})

def home_listado_nivelTDAH_g(request, slug1, slug2):
    # el slug1 es del usuario y slug2 de resultado
    nivelTDAH = GradoTDAH.objects.all()
    reporte = Reportes.objects.all()
    return render(request, 'home_comun/listado_nivelTDAH.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug1, 'slug1': slug2})

def home_listado_nivelTDAH_t(request, slug):
    try:
        # Buscamos si el slug pertenece a una categoría
        categoria_ob = Categoria.objects.get(slug_categoria=slug)
        # Buscamos el grado que se asocia a esa categoría
        grado_tdah_ob = categoria_ob.grado_tdah_f
        # Validamos la existencia
        usuario_tecnico = grado_tdah_ob.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)
        # Obtenemos los datos requeridos
        nivelTDAH = GradoTDAH.objects.all()
        reporte = Reportes.objects.all()
        return render(request, 'home_tecnico/listado_nivelTDAH_t.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug_encriptado, 'ob_tecnico': usuario_tecnico.nombre})

    except (Categoria.DoesNotExist, GradoTDAH.DoesNotExist):
        try:
            # Buscamos que si el slug pertenece a un Grado TDAH
            grado_tdah = GradoTDAH.objects.get(slug_grado=slug)
            # Validamos la existencia
            usuario_tecnico = grado_tdah.usuario_tecnico
            slug_usuario_tecnico = usuario_tecnico.slug
            # Encriptamos el slug
            slug_encriptado = encriptar(slug_usuario_tecnico)
            # Obtenemos los datos requeridos
            nivelTDAH = GradoTDAH.objects.all()
            reporte = Reportes.objects.all()
            return render(request, 'home_tecnico/listado_nivelTDAH_t.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug_encriptado, 'ob_tecnico': usuario_tecnico.nombre})

        except GradoTDAH.DoesNotExist:
            slugt_d_lista = desencriptar(slug)
            ob_tecnico = get_object_or_404(UsuarioTecnico, slug=slugt_d_lista)
            nivelTDAH = GradoTDAH.objects.all()
            reporte = Reportes.objects.all()
            return render(request, 'home_tecnico/listado_nivelTDAH_t.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug, 'ob_tecnico': ob_tecnico.nombre})

    
def home_listado_nivelTDAH_t_c(request, slug):
    try:
        grado_tdah = GradoTDAH.objects.get(slug_grado=slug)
        usuario_tecnico = grado_tdah.usuario_tecnico
        slug_usuario_tecnico = usuario_tecnico.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_tecnico)
        # Obtenemos los datos requeridos
        nivelTDAH = GradoTDAH.objects.all()
        reporte = Reportes.objects.all()

    except ObjectDoesNotExist:
        # Manejar la excepción si no se encuentra el registro de GradoTDAH o UsuarioTecnico asociado
        return render(request, 'error/404.html', {})

    return render(request, 'home_tecnico/listado_nivelTDAH_t.html', {'nivelTDAH': nivelTDAH, 'reporte': reporte, 'slug': slug_encriptado, 'ob_tecnico': usuario_tecnico})

def home_listado_nivelTDAH_p(request, slug):
    try:
        slugt_d_lista = desencriptar(slug)
        usuario_ = get_object_or_404(Paciente, slug=slugt_d_lista)
        nombre_usuario = usuario_.nombre
        # Obtenemos los datos necesarios
        nivelTDAH = GradoTDAH.objects.all()
        return render(request, 'home_paciente/listado_nivelTDAH_p.html', {'nivelTDAH': nivelTDAH, 'usuario': nombre_usuario, 'slug': slug})
    
    except ObjectDoesNotExist:
        return render(request, 'error/404.html', {})
    

#   Listado de categorias	

def home_listado_categoria_t(request, slug):
    try:
        # Se obtiene el objeto asociado a ese slug
        ob_gradoTdah = GradoTDAH.objects.get(slug_grado=slug)
        ob_user = ob_gradoTdah.usuario_tecnico
        categoria = Categoria.objects.filter(grado_tdah_f=ob_gradoTdah)
        return render(request, 'register/registerCategoria/listado_categoria_t.html', {'categoria': categoria, 'slug': ob_gradoTdah.slug_grado, 'ob_grado': ob_gradoTdah.nombre_nivel, 'usuario': ob_user.nombre})

    except GradoTDAH.DoesNotExist:
        try:
            # el slug es de categoria
            ob_categoria = Categoria.objects.get(slug_categoria=slug)
            ob_gradoTdah = ob_categoria.grado_tdah_f
            ob_user = ob_gradoTdah.usuario_tecnico
            categoria = Categoria.objects.filter(grado_tdah_f=ob_gradoTdah)
            return render(request, 'register/registerCategoria/listado_categoria_t.html', {'categoria': categoria, 'slug': ob_gradoTdah.slug_grado, 'ob_grado': ob_gradoTdah.nombre_nivel, 'usuario': ob_user.nombre})
        
        except:
            categoria = Categoria.objects.all()
            return render(request, 'register/registerCategoria/listado_categoria_t.html', {'categoria': categoria, 'slug': slug})

def home_listado_categoria_t_general(request, slug):
    slug_descriptado = desencriptar(slug)
    usuario = get_object_or_404(UsuarioTecnico, slug=slug_descriptado)
    categoria = Categoria.objects.all()
    return render(request, 'register/registerCategoria/listado_categoria_t_general.html', {'categoria': categoria, 'slug': slug, 'usuario': usuario.nombre})


def home_listado_categoria_c(request, slug, slug2):
    # slug= usuario slug2=nivel
    # Obtenemos el usuario
    slug_descriptado = desencriptar(slug)
    usuario = get_object_or_404(UsuarioComun, slug=slug_descriptado)
    try:
        # Obtenemos el nivel
        ob_nivel = GradoTDAH.objects.get(slug_grado=slug2)
        categoria = Categoria.objects.filter(grado_tdah_f=ob_nivel)
        return render(request, 'register/registerCategoria/listado_categoria_c.html', {'categoria': categoria, 'nivel': ob_nivel.nombre_nivel, 'usuario': usuario.nombre,'slug': slug, 'slug2': slug2})
    
    except GradoTDAH.DoesNotExist:
        try:
            # slug= usuario slug2=categoria
            ob_categoria = Categoria.objects.get(slug_categoria=slug2)
            ob_nivel = ob_categoria.grado_tdah_f
            categoria = Categoria.objects.filter(grado_tdah_f=ob_nivel)
            return render(request, 'register/registerCategoria/listado_categoria_c.html', {'categoria': categoria, 'nivel': ob_nivel.nombre_nivel, 'usuario': usuario.nombre,  'slug': slug, 'slug2': slug2})
    
        except:
            error_message = "No se encontraron categorias asociadas a este nivel"
            return render(request, 'error/404.html', {'error': error_message})

def home_listado_categoria_p(request, slug, slug2):
    # slug= usuario slug2=nivel
    # Obtenemos el usuario
    slug_descriptado = desencriptar(slug)
    usuario = get_object_or_404(Paciente, slug=slug_descriptado)
    try:
        ob_nivel = GradoTDAH.objects.get(slug_grado=slug2)
        categoria = Categoria.objects.filter(grado_tdah_f=ob_nivel)
        return render(request, 'register/registerCategoria/listado_categoria_p.html', {'categoria': categoria, 'nivel': ob_nivel.nombre_nivel, 'usuario': usuario.nombre, 'slug': slug, 'slug2': slug2})
    
    except GradoTDAH.DoesNotExist:
        try:
            # slug1= usuario slug2=categoria
            ob_categoria = Categoria.objects.get(slug_categoria=slug2)
            ob_nivel = ob_categoria.grado_tdah_f
            categoria = Categoria.objects.filter(grado_tdah_f=ob_nivel)
            return render(request, 'register/registerCategoria/listado_categoria_p.html', {'categoria': categoria,  'nivel': ob_nivel.nombre_nivel, 'usuario': usuario.nombre, 'slug': slug, 'slug2': slug2})
    
        except:
            error_message = "No se encontraron categorias asociadas a este nivel"
            return render(request, 'error/404.html', {'error': error_message})

# Listado de cursos

def listado_cursos_c(request, slug):
    try:
        # El slug es del Curso
        curso = Curso.objects.get(slug_curso=slug)
        # Validamos la existencia
        usuario_comun = curso.usuario_comun
        slug_usuario_comun = usuario_comun.slug
        # Encriptamos el slug
        slug_encriptado = encriptar(slug_usuario_comun)
        cursos = Curso.objects.filter(usuario_comun=usuario_comun)
        return render(request, 'register/registerCurso/listado_curso_c.html', {'curso': cursos, 'slug': slug_encriptado, 'usuario': usuario_comun.nombre})
    
    except Curso.DoesNotExist:
        cursos = Curso.objects.all()
        return render(request, 'register/registerCurso/listado_curso_c.html', {'curso': cursos, 'slug': slug})

def listado_cursos_t(request, slug):
    try:
        # Buscamos el usuario
        slug_descriptado = desencriptar(slug)
        usuario = get_object_or_404(UsuarioTecnico, slug=slug_descriptado)
        nombre = usuario.nombre
        # Obtenemos los cursos
        curso = Curso.objects.all()
        return render(request, 'register/registerCurso/listado_curso_t.html', {'curso': curso, 'usuario': nombre, 'slug': slug})
    
    except Curso.DoesNotExist:
        mensaje = "No se encontraron cursos"
        return render(request, 'error/404.html', {'error': mensaje})

def listado_cursos_p(request, slug):
    try:
        # Buscamos el usuario
        slug_descriptado = desencriptar(slug)
        usuario = get_object_or_404(Paciente, slug=slug_descriptado)
        nombre = usuario.nombre
        # Obtenemos los cursos  
        curso = Curso.objects.all()
        return render(request, 'register/registerCurso/listado_curso_p.html', {'curso': curso, 'usuario': nombre , 'slug': slug})

    except Curso.DoesNotExist:
        mensaje = "No se encontraron cursos"
        return render(request, 'error/404.html', {'error': mensaje})
    
    
# Listado de contenido

def home_listado_contenido_t(request, slug):
    try:
        contenido_ob = Contenido.objects.get(slug_contenido=slug)
        categoria_ob = contenido_ob.categoria
        # Buscamos el usuario
        usuario = categoria_ob.grado_tdah_f.usuario_tecnico
        nombre_usuario = usuario.nombre
        if categoria_ob:
            # Validamos la existencia
            contenido = Contenido.objects.filter(categoria=categoria_ob)
            return render(request, 'register/registerContenido/listado_contenido_t.html', {'contenido': contenido, 'slug': categoria_ob.slug_categoria, 'ob_categoria': categoria_ob.nombre_categoria, 'usuario': nombre_usuario})
    
    except Contenido.DoesNotExist:
        # slug es de categoria
        categoria_ob_ = Categoria.objects.get(slug_categoria=slug)
        contenido = Contenido.objects.filter(categoria=categoria_ob_)
        # Buscamos el usuario
        usuario = categoria_ob.grado_tdah_f.usuario_tecnico
        nombre_usuario = usuario.nombre
        return render(request, 'register/registerContenido/listado_contenido_t.html', {'contenido': contenido, 'slug': slug, 'ob_categoria': categoria_ob_.nombre_categoria, 'usuario': nombre_usuario})

    except Categoria.DoesNotExist:
        contenido = Contenido.objects.all()
        return render(request, 'register/registerContenido/listado_contenido_t.html', {'contenido': contenido, 'slug': slug})

def home_listado_contenido_c(request, slug, slug2):
    # slug= usuario slug2=categoria
    slug_des = desencriptar(slug)
    usuario = get_object_or_404(Paciente, slug=slug_des)
    nombre = usuario.nombre
    try:
        ob_categoria = Categoria.objects.get(slug_categoria=slug2)
        contenido = Contenido.objects.filter(categoria=ob_categoria)
        return render(request, 'register/registerContenido/listado_contenido_c.html', {'contenido': contenido, 'ob_categoria': ob_categoria.nombre_categoria, 'usuario': nombre, 'slug': slug, 'slug2': slug2})
    
    except Categoria.DoesNotExist:
        error_message = "No se encontraron contenidos asociadas a este nivel"
        return render(request, 'error/404.html', {'error': error_message})

def home_listado_contenido_p(request, slug, slug2):
    # slug1= usuario slug2=categoria
    slug_des = desencriptar(slug)
    usuario = get_object_or_404(Paciente, slug=slug_des)
    nombre = usuario.nombre
    try:
        ob_categoria = Categoria.objects.get(slug_categoria=slug2)
        contenido = Contenido.objects.filter(categoria=ob_categoria)
        return render(request, 'register/registerContenido/listado_contenido_p.html', {'contenido': contenido, 'ob_categoria': ob_categoria.nombre_categoria, 'usuario': nombre, 'slug': slug, 'slug2': slug2})
    
    except Categoria.DoesNotExist:
        error_message = "No se encontraron contenidos asociadas a este nivel"
        return render(request, 'error/404.html', {'error': error_message})

# Listado de peticiones

def home_listado_peticiones_t(request, slug):
    try:
        # Buscamos el usuario
        slug_descriptado = desencriptar(slug)
        usuarioT_ob = UsuarioTecnico.objects.get(slug=slug_descriptado)
        # Obtenemos las peticiones
        peticion_ob = Peticion.objects.all()
        return render(request, 'register/registerPeticion/listado_peticion_t.html', {'peticion': peticion_ob, 'slug': slug, 'usuario': usuarioT_ob.nombre})
    except UsuarioTecnico.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        return render(request, 'error/404.html', {})

def home_listado_peticiones_c(request, slug):
    try:
        peticion = Peticion.objects.get(slug_peticion=slug)
        usuario_comun = peticion.usuario_comun
        slug_encriptado = encriptar(usuario_comun.slug)

        peticiones = Peticion.objects.filter(usuario_comun=usuario_comun)
        return render(request, 'register/registerPeticion/listado_peticion_c.html', {'peticion': peticiones, 'slug': slug_encriptado, 'usuario': usuario_comun.nombre})

    except Peticion.DoesNotExist:
        try:
            slug_des = desencriptar(slug)
            usuario_comun = get_object_or_404(UsuarioComun, slug=slug_des)
            peticion = Peticion.objects.filter(usuario_comun=usuario_comun)
            return render(request, 'register/registerPeticion/listado_peticion_c.html', {'peticion': peticion, 'slug': slug, 'usuario': usuario_comun.nombre})

        except UsuarioComun.DoesNotExist:
            # Manejar la excepción si no se encuentra el registro de UsuarioComun
            error_message = "No existe el registro de UsuarioComun"
            return render(request, 'error/404.html', {'error': error_message})


# Listado de salas

def home_listado_sala_t(request, slug):
    try:
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioTecnico.objects.get(slug=slug_des)
        sala_ob = Sala.objects.all()
        return render(request, 'register/registerSala/listado_sala_t.html', {'sala': sala_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
    except UsuarioTecnico.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        return render(request, 'error/404.html', {})

def home_listado_sala_c(request, slug):
    try:
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        salas_ob = Sala.objects.filter(usuario_comun=usuarioC_ob)
        return render(request, 'register/registerSala/listado_sala_c.html', {'sala': salas_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
        
    except UsuarioComun.DoesNotExist:
        try:
            sala = Sala.objects.get(slug_sala=slug)
            usuario_comun = sala.usuario_comun
            sala_ob = Sala.objects.filter(usuario_comun=usuario_comun)
            return render(request, 'register/registerSala/listado_sala_c.html', {'sala': sala_ob, 'slug': slug, 'usuario': usuario_comun.nombre})
    
        except Sala.DoesNotExist:
            # Manejar la excepción si no se encuentra el registro de Sala
            return render(request, 'error/404.html', {})


# Listados de Reportes

def home_listado_reportes_c(request, slug):
    try:
        reporte = Reportes.objects.get(slug_reporte=slug)
        usuario_comun = reporte.usuario_comun
        slug_encriptado = encriptar(usuario_comun.slug)
        reporte_ob = Reportes.objects.filter(usuario_comun=usuario_comun)
        return render(request, 'register/registerReportes/listado_reporte_c.html', {'reporte': reporte_ob, 'slug': slug_encriptado, 'usuario': usuario_comun.nombre})
    
    except Reportes.DoesNotExist:
        try:
            slug_des = desencriptar(slug)
            usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
            reportes_ob = Reportes.objects.filter(usuario_comun=usuarioC_ob)
            return render(request, 'register/registerReportes/listado_reporte_c.html', {'reporte': reportes_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
    
        except UsuarioComun.DoesNotExist:
            # Manejar la excepción si no se encuentra el registro de UsuarioComun
            return render(request, 'error/404.html', {})

def home_listado_reportes_t(request, slug):
    try:
        slug_descriptado = desencriptar(slug)
        usuarioC_ob = UsuarioTecnico.objects.get(slug=slug_descriptado)
        reporte_ob = Reportes.objects.all()
        return render(request, 'register/registerReportes/listado_reporte_t.html', {'reporte': reporte_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
    except UsuarioTecnico.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        return render(request, 'error/404.html', {})


# Listado de resultados

def home_listado_resultados_c(request, slug):
    try:
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        resultado_ob = Resultados.objects.all()
        return render(request, 'register/registerResultados/listado_resultado_c.html', {'resultado': resultado_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
    
    except ObjectDoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        return render(request, 'error/404.html', {})

def home_listado_resultados_t(request, slug):
    try:
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioTecnico.objects.get(slug=slug_des)
        resultado_ob = Resultados.objects.all()
        return render(request, 'register/registerResultados/listado_resultado_t.html', {'resultado': resultado_ob, 'slug': slug, 'usuario': usuarioC_ob.nombre})
    except UsuarioTecnico.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        return render(request, 'error/404.html', {})
#
#
#
#
# PERFILES
#
#
#
#

def profile_user_paciente(request, slug):
    slug_d = desencriptar(slug)
    # Realizar la consulta al modelo UserPaciente
    user_paciente = get_object_or_404(Paciente, slug=slug_d)
    return render(request, 'home_paciente/perfil_user_paciente.html', {'user_paciente': user_paciente, 'slug': slug})

def profile_user_comun(request, slug):
    slug_c = desencriptar(slug)
    print(slug_c)
    # Realizar la consulta al modelo Usuario Comun
    #user_comun = UsuarioComun.objects.get(slug=slug_c)
    user_comun = get_object_or_404(UsuarioComun, slug=slug_c)
    return render(request, 'home_comun/perfil_user_comun.html', {'user_comun': user_comun, 'slug': slug})

def profile_user_tecnico(request, slug):
    slug_t = desencriptar(slug)
    # Realizar la consulta al modelo Usuario Tecnico
    user_tecnico = get_object_or_404(UsuarioTecnico, slug=slug_t)
    return render(request, 'home_tecnico/perfil_user_tecnico.html', {'user_tecnico': user_tecnico, 'slug': slug})

def perfil_user(request, slug):
    slug_c = desencriptar(slug)
    print(slug_c)
    # Realizar la consulta al modelo Usuario Comun
    user_comun = UsuarioComun.objects.get(slug=slug_c)
    return render(request, 'home_comun/perfil_user_comun.html', {'user_comun': user_comun, 'slug': slug})


#
#
#
#
# Detalles de registros
#
#
#
#
#
#

def detalle_contenido_c(request, slug, slug2):
    # slug=usuario slug2=contenido
    # Si viene de usuario comun recibe slug de usuario comun y contenido
    # Si viene de paciente recibe slug de paciente y contenido
    # Si viene de usuario tecnico recibe slug de contenido

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        contenido_ob = Contenido.objects.get(slug_contenido=slug2)
        categoria_ob = contenido_ob.categoria

        return render(request, 'register/registerContenido/detalle_contenido.html', {'slug': slug, 'slug2': categoria_ob.slug_categoria, 'contenido': contenido_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        try:
            # Paciente
            slug_des = desencriptar(slug)
            paciente_ob = Paciente.objects.get(slug=slug_des)
            contenido_ob = Contenido.objects.get(slug_contenido=slug2)
            categoria_ob = contenido_ob.categoria

            return render(request, 'register/registerContenido/detalle_contenido.html', {'slug': slug, 'slug2': categoria_ob.slug_categoria, 'contenido': contenido_ob, 'usuario': paciente_ob})

        except:
            # Usuario tecnico
            conten_ob = Contenido.objects.get(slug_contenido=slug2)
            categoria_ob = conten_ob.categoria
            ob_nivelTDA = categoria_ob.grado_tdah_f
            usuariot_ob = ob_nivelTDA.usuario_tecnico

            return render(request, 'register/registerContenido/detalle_contenido.html', {'slug': categoria_ob.slug_categoria, 'slug2': categoria_ob.slug_categoria, 'contenido': conten_ob, 'usuario': usuariot_ob})
        
def ver_detalle_reporte_c(request, slug, slug2):
    # slug=usuario slug2=reporte
    # Si viene de usuario comun recibe slug de usuario comun y reporte
    # Si viene de usuario tecnico recibe slug de reporte

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        reporte_ob = Reportes.objects.get(slug_reporte=slug2)
        
        return render(request, 'register/registerReporte/detalle_reporte.html', {'slug': slug, 'slug2': reporte_ob.slug_reporte, 'reporte': reporte_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        # Usuario tecnico
        reporte_ob = Reportes.objects.get(slug_reporte=slug2)
        slug_des = desencriptar(slug)
        usuariot_ob = UsuarioTecnico.get(slug=slug_des)

        return render(request, 'register/registerReporte/detalle_reporte.html', {'slug': slug, 'slug2': reporte_ob.slug_reporte, 'reporte': reporte_ob, 'usuario': usuariot_ob})

            
def detalle_categoria_c(request, slug, slug2):
    # slug=usuario slug2=categoria
    # Si viene de usuario comun recibe slug de usuario comun y categoria
    # Si viene de paciente recibe slug de paciente y categoria
    # Si viene de usuario tecnico recibe slug de categoria

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        categoria_ob = Categoria.objects.get(slug_categoria=slug2)

        return render(request, 'register/registerCategoria/detalle_probando.html', {'slug': slug, 'slug2': categoria_ob.slug_categoria, 'categoria': categoria_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        try:
            # Paciente
            slug_des = desencriptar(slug)
            paciente_ob = Paciente.objects.get(slug=slug_des)
            categoria_ob = Categoria.objects.get(slug_categoria=slug2)

            return render(request, 'register/registerCategoria/detalle_probando.html', {'slug': slug, 'slug2': categoria_ob.slug_categoria, 'categoria': categoria_ob, 'usuario': paciente_ob})

        except:
            # Usuario tecnico
            categoria_ob = Categoria.objects.get(slug_categoria=slug2)
            ob_nivelTDA = categoria_ob.grado_tdah_f
            usuariot_ob = ob_nivelTDA.usuario_tecnico

            return render(request, 'register/registerCategoria/detalle_probando.html', {'slug': slug2, 'slug2': slug2, 'categoria': categoria_ob, 'usuario': usuariot_ob})

def detalle_curso_(request, slug, slug2):
    # slug=usuario slug2=nivel
    # Si viene de usuario comun recibe slug de usuario comun y nivel
    # Si viene de paciente recibe slug de paciente y nivel
    # Si viene de usuario tecnico recibe slug de nivel

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        curso_ob = Curso.objects.get(slug_curso=slug2)

        return render(request, 'register/registerCurso/detalle_curso.html', {'slug': slug, 'slug2': curso_ob.slug_curso, 'curso': curso_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        try:
            # Paciente
            slug_des = desencriptar(slug)
            paciente_ob = Paciente.objects.get(slug=slug_des)
            curso_ob = Curso.objects.get(slug_curso=slug2)

            return render(request, 'register/registerCurso/detalle_curso.html', {'slug': slug, 'slug2': curso_ob.slug_curso, 'curso': curso_ob, 'usuario': paciente_ob})

        except:
            # Usuario tecnico
            slug_des = desencriptar(slug)
            curso_ob = Curso.objects.get(slug_curso=slug2)
            usuariot_ob = UsuarioTecnico.objects.get(slug=slug_des)

            return render(request, 'register/registerCurso/detalle_curso.html', {'slug': slug, 'slug2': curso_ob.slug_curso, 'curso': curso_ob, 'usuario': usuariot_ob})

def detalle_peticion(request, slug, slug2):
    # slug=usuario slug2=peticion
    # Si viene de usuario comun recibe slug de usuario comun y peticion
    # Si viene de usuario tecnico recibe slug de peticion

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        peticion_ob = Peticion.objects.get(slug_peticion=slug2)

        return render(request, 'register/registerPeticion/detalle_peticion.html', {'slug': slug, 'slug2': peticion_ob.slug_peticion, 'peticion': peticion_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        # Usuario tecnico
        peticion_ob = Peticion.objects.get(slug_peticion=slug2)
        slug_des = desencriptar(slug)
        usuariot_ob = UsuarioTecnico.get(slug=slug_des)

        return render(request, 'register/registerPeticion/detalle_peticion.html', {'slug': slug, 'slug2': slug, 'peticion': peticion_ob, 'usuario': usuariot_ob})

def ver_detalle_resultado(request, slug, slug2):
    # slug=usuario slug2=resultado
    # Si viene de usuario comun recibe slug de usuario comun y resultado
    # Si viene de usuario tecnico recibe slug de resultado

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        resultado_ob = Resultados.objects.get(slug_resultado=slug2)

        return render(request, 'register/registerResultados/detalle_resultado.html', {'slug': slug, 'slug2': resultado_ob.slug_resultado, 'resultado': resultado_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        # Usuario tecnico
        resultado_ob = Resultados.objects.get(slug_resultado=slug2)
        slug_des = desencriptar(slug)
        usuariot_ob = UsuarioTecnico.get(slug=slug_des)

        return render(request, 'register/registerResultados/detalle_resultado.html', {'slug': slug, 'slug2': slug, 'resultado': resultado_ob, 'usuario': usuariot_ob})
    
def detalle_nivel(request, slug, slug2):
    # slug=usuario slug2=nivel
    # Si viene de usuario comun recibe slug de usuario comun y nivel
    # Si viene de paciente recibe slug de paciente y nivel
    # Si viene de usuario tecnico recibe slug de nivel

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        nivel_ob = GradoTDAH.objects.get(slug_grado=slug2)

        return render(request, 'register/registerTDAH/detalle_nivel.html', {'slug': slug, 'slug2': nivel_ob.slug_grado, 'nivel': nivel_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        try:
            # Paciente
            slug_des = desencriptar(slug)
            paciente_ob = Paciente.objects.get(slug=slug_des)
            nivel_ob = GradoTDAH.objects.get(slug_grado=slug2)

            return render(request, 'register/registerTDAH/detalle_nivel.html', {'slug': slug, 'slug2': nivel_ob.slug_grado, 'nivel': nivel_ob, 'usuario': paciente_ob})

        except:
            # Usuario tecnico
            nivel_ob = GradoTDAH.objects.get(slug_grado=slug2)
            usuariot_ob = nivel_ob.usuario_tecnico

            return render(request, 'register/registerTDAH/detalle_nivel.html', {'slug': slug2, 'slug2': slug2, 'nivel': nivel_ob, 'usuario': usuariot_ob})

def detalle_sala(request, slug, slug2):
    # slug=usuario slug2=sala
    # Si viene de usuario comun recibe slug de usuario comun y resultado
    # Si viene de usuario tecnico recibe slug de resultado

    try:
        # Usuario comun
        slug_des = desencriptar(slug)
        usuarioC_ob = UsuarioComun.objects.get(slug=slug_des)
        sala_ob = Sala.objects.get(slug_sala=slug2)

        return render(request, 'register/registersala/detalle_sala.html', {'slug': slug, 'slug2': sala_ob.slug_sala, 'sala': sala_ob, 'usuario': usuarioC_ob})

    except UsuarioComun.DoesNotExist:
        # Manejar la excepción si no se encuentra el registro de UsuarioComun
        # Usuario tecnico
        sala_ob = Sala.objects.get(slug_sala=slug2)
        slug_des = desencriptar(slug)
        usuariot_ob = UsuarioTecnico.get(slug=slug_des)

        return render(request, 'register/registersala/detalle_sala.html', {'slug': slug, 'slug2': sala_ob.slug_sala, 'sala': sala_ob, 'usuario': usuariot_ob})
    
#
#
#
#
# Registrarse en Curso
#
#
#
#
#
#
def registrarseCurso(request, slug, slug2):
    # El slug es del paciente
    # El slug2 es del curso
    try:
        curso_ob = Curso.objects.get(slug_curso=slug2)
        slug_desc = desencriptar(slug)
        paciente_ob = Paciente.objects.get(slug=slug_desc)
        # Registramos el usuario en el curso
        detalle_c_p = DetallePacienteCurso.objects.create(
            paciente=paciente_ob,
            curso=curso_ob
        )
        detalle_c_p.save() # Se guarda el registro
        url = reverse('listado_nivel_TDAH_p', kwargs={'slug': slug})
        return redirect(url)
    except IntegrityError:
        error_message = "No se puede registrar al curso"
        return render(request, 'error/404.html', {'error': error_message, 'slug':slug})


