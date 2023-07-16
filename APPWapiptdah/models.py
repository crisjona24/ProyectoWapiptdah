from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.
'''
class Dominio(enum.Enum):
    Leve = 'Leve'
    Moderado = 'Moderado'
    Critico = 'Critico'

class Rol(enum.Enum):
    UsuarioComun = 'UsuarioComun'
    UsuarioTecnico = 'UsuarioTecnico'
    Paciente = 'Paciente'

class AreaEstudio(enum.Enum):
    Licenciatura = 'Licenciatura'
    Psicopedagogía = 'Psicopedagogía'
    Parvularia = 'Parvularia'

class AreaOperacion(enum.Enum):
    Psicopedagogia = 'Psicopedagogia'
    TecnicoInformatico = 'TecnicoInformatico'

class Persona(models.Model):
    nombre = models.CharField(max_length=140, blank=False, null=True)
    apellido = models.CharField(max_length=140, blank=False, null=True)
    correoElectronico = models.EmailField(unique=True, blank=True, null=True)
    numeroCelular = models.CharField(max_length=10, blank=False, null=True)
    DNI = models.CharField(max_length=10, blank=False, unique=True, null=True)
    direccion = models.CharField(max_length=140, blank=False, null=True)
    fechaNacimiento = models.DateField()
    actividad = models.CharField(max_length=20, choices=[(actividad.name, actividad.value) for actividad in Rol])

class UsuarioComun(models.Model):
    areaEstudio = models.CharField(max_length=20, choices=[(area.name, area.value) for area in AreaEstudio])
    especialidad = models.CharField(max_length=140, blank=False, null=True)
    genero = models.CharField(max_length=140, blank=False, null=True)
    nivelFormacion = models.CharField(max_length=140, blank=False, null=True)
    tituloUniversitario = models.CharField(max_length=140, blank=False, null=True)

    def validate_positive(value):
        if value < 0:
            raise models.ValidationError("El valor debe ser positivo")
    experiencia = models.IntegerField(default=0, validators=[validate_positive])

class Paciente(models.Model):
    antecedenteMedico = models.TextField(max_length=50, blank=False, null=True)
    contactoEmergencia = models.CharField(max_length=80, blank=False, null=True)
    edad = models.IntegerField()

class UsuarioTecnico(models.Model):
    especialidad = models.CharField(max_length=50, blank=False, null=True)
    identificacion = models.IntegerField()
    tituloUniversitario = models.CharField(max_length=50, blank=False, null=True)
    areaOperacion = models.CharField(max_length=20, choices=[(operacion.name, operacion.value) for operacion in AreaOperacion])

class Cuenta(models.Model):
    user = models.CharField(max_length=15, blank=False, null=True, unique=True)
    contra = models.CharField(max_length=15, blank=False, null=True)
    estado = models.BooleanField(default=True)

class Curso(models.Model):
    nombreCurso = models.CharField(max_length=80, blank=False, null=True)
    descripcionCurso = models.TextField(max_length=50, blank=False, null=True)
    estadoCurso = models.BooleanField(default=True)
    fechaRegistro = models.DateField()

class GradoTDAH(models.Model):
    nombreNivel = models.CharField(max_length=80, blank=False, null=True)
    numeroCategorias = models.IntegerField()
    gradoDificultad = models.CharField(max_length=80, blank=False, null=True)
    descripcionGrado = models.CharField(max_length=80, blank=False, null=True)
    fechaRegistro = models.DateField()

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=80, blank=False, null=True)
    numTest = models.IntegerField()
    gradoDificultad = models.CharField(max_length=80, blank=False, null=True)
    descripcionCategoria = models.TextField(max_length=50, blank=False, null=True)
    fechaRegistro = models.DateField()

class Contenido(models.Model):
    nombreContenido = models.CharField(max_length=80, blank=False, null=True)
    descripcionContenido = models.TextField(max_length=50, blank=False, null=True)
    identificadorContenido = models.IntegerField()
    estadoContenido = models.BooleanField(default=True)
    contenido = models.CharField(max_length=80, blank=False, null=True)
    fechaRegistro = models.DateField()
    dominio = models.CharField(max_length=20, choices=[(dominio.name, dominio.value) for dominio in Dominio])

class Resultados(models.Model):
    anotaciones = models.TextField(max_length=50, blank=True, null=True)
    porcentajeResuelto = models.CharField(max_length=80, blank=True, null=True)
    fechaRegistro = models.DateField()

class Reportes(models.Model):
    fechaReporte = models.DateField()

class DetalleContenidoResuleto(models.Model):
    fechaResolver = models.DateField()
    puntuacion = models.CharField(max_length=80, blank=False, null=True)
    porcentajeResuelto = models.CharField(max_length=80, blank=False, null=True)

class Sala(models.Model):
    anotaciones = models.CharField(max_length=80, blank=False, null=True)
    fechaRegistroSala = models.DateField()
    estadoSala = models.BooleanField(default=True)
    canceladaSala = models.BooleanField(default=False)

class Peticion(models.Model):
    estadoPeticion = models.BooleanField(default=False)
    fechaRegistroPeticion = models.DateField()
    motivoPeticion = models.CharField(max_length=80, blank=False, null=True)
    peticion = models.TextField(max_length=50, blank=True, null=True)
    tipoPeticion = models.CharField(max_length=80, blank=False, null=True)


'''
'''
class Persona(models.Model):
    nombre = models.CharField(max_length=140)
    apellido = models.CharField(max_length=140)
    correo_electronico = models.EmailField(unique=True, blank=True)
    numero_celular = models.CharField(max_length=10, blank=False, null=True)
    direccion = models.CharField(max_length=140)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8)], unique=True)
    fecha_nacimiento = models.DateField()
    actividad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
'''
    
class UsuarioComun(models.Model):
    nombre = models.CharField(max_length=140)
    apellido = models.CharField(max_length=140)
    correo_electronico = models.EmailField(unique=True, blank=True,)
    numero_celular = models.CharField(max_length=10, blank=False, null=True)
    genero = models.CharField(max_length=100)
    area_estudio = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8)], unique=True)
    fecha_nacimiento = models.DateField()
    actividad = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    is_usuario_comun = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre + "-" + self.apellido)
        super(UsuarioComun, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.genero} {self.area_estudio}"


class UsuarioTecnico(models.Model):
    nombre = models.CharField(max_length=140)
    apellido = models.CharField(max_length=140)
    correo_electronico = models.EmailField(unique=True, blank=True)
    numero_celular = models.CharField(max_length=10, blank=False, null=True)
    identificacion = models.CharField(max_length=10, unique=True)
    area_operacion = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16, validators=[MinLengthValidator(8)], unique=True)
    fecha_nacimiento = models.DateField()
    actividad = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    is_usuario_tecnico = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre + "-" + self.apellido)
        super(UsuarioTecnico, self).save(*args, **kwargs)

    def clean(self):
        if int(self.identificacion) < 0:
            raise ValidationError("La identificación debe ser un valor positivo")

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.area_operacion}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=140)
    apellido = models.CharField(max_length=140)
    correo_electronico = models.EmailField(unique=True, blank=True)
    numero_celular = models.CharField(max_length=10, blank=False, null=True)
    contacto_emergencia = models.CharField(max_length=10, blank=False, null=True)
    edad = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16, unique=True)
    fecha_nacimiento = models.DateField()
    actividad = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    is_paciente = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre + "-" + self.apellido)
        super(Paciente, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.contacto_emergencia} {self.edad}"


##MODELO DE GRADO DE TDAH
class GradoTDAH(models.Model):
    nombre_nivel = models.CharField(max_length=80, blank=False, null=True, unique=True)
    numero_categorias = models.IntegerField()
    grado_dificultad = models.CharField(max_length=80, blank=False, null=True)
    descripcion_grado = models.CharField(max_length=80, blank=False, null=True)
    fecha_registro_grado = models.DateField(auto_now=True)
    slug_grado = models.SlugField(unique=True, blank=True)
    # Agregar la clave foránea a UsuarioTecnico
    usuario_tecnico = models.ForeignKey(UsuarioTecnico, on_delete=models.CASCADE, related_name='grados_tdah', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_grado = slugify(self.nombre_nivel + "-" + self.grado_dificultad)
        super(GradoTDAH, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_nivel} {self.numero_categorias} {self.fecha_registro_grado}"

#MODELO DE CURSO
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=80, blank=False, null=True, unique=True)
    descripcion_curso = models.TextField(max_length=50, blank=False, null=True)
    estado_curso = models.BooleanField(default=True)
    fecha_registro_curso = models.DateField(auto_now=True)
    slug_curso = models.SlugField(unique=True, blank=True)
    # Agregar la clave foránea a Usuario comun
    usuario_comun = models.ForeignKey(UsuarioComun, on_delete=models.CASCADE, related_name='cursos', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_curso = slugify(self.nombre_curso)
        super(Curso, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_curso} {self.estado_curso} {self.fecha_registro_curso}"

class DetallePacienteCurso(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, related_name='paciente', blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, related_name='curso', blank=True, null=True)
    estado_detalle = models.BooleanField(default=True)
    fecha_registro_detalle= models.DateField(auto_now=True)

#MODELO DE CATEGORIA
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=80, blank=False, null=True)
    num_test = models.IntegerField()
    grado_dificultad = models.CharField(max_length=80, blank=False, null=True)
    descripcion_categoria = models.TextField(max_length=50, blank=False, null=True)
    fecha_registro_categoria= models.DateField(auto_now=True)
    estado_categoria = models.BooleanField(default=True)
    slug_categoria = models.SlugField(unique=True, blank=True)
    grado_tdah_f = models.ForeignKey(GradoTDAH, on_delete=models.CASCADE, related_name='categorias', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_categoria = slugify(self.nombre_categoria + "-" + self.grado_dificultad)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_categoria} {self.num_test} {self.fecha_registro_categoria}"

#MODELO DE CONTENIDO
class Contenido(models.Model):
    nombre = models.CharField(max_length=80, blank=False, null=True)
    descripcion = models.TextField(blank=False, null=True)
    identificador_contenido = models.IntegerField(unique=True)
    contenido = models.CharField(max_length=80, blank=False, null=True)
    dominio = models.CharField(max_length=80, blank=False, null=True)
    fecha_registro_contenido = models.DateField(auto_now=True)
    estado_contenido = models.BooleanField(default=True)
    slug_contenido = models.SlugField(unique=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='contenidos', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_contenido = slugify(self.nombre + "-" + self.dominio)
        super(Contenido, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.dominio} {self.fecha_registro_contenido}"

#MODELO DE RESULTADOS
class Resultados(models.Model):
    anotaciones = models.TextField(max_length=50, blank=True, null=True)
    calificacion = models.CharField(max_length=80, blank=True, null=True)
    fecha_registro_resultado = models.DateField(auto_now=True)
    slug_resultado = models.SlugField(unique=True, blank=True)
    fecha_edit_resultado = models.DateField(blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, related_name='resultados', blank=True, null=True)
    contenido = models.ForeignKey(Contenido, on_delete=models.SET_NULL, related_name='resultados_c', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_resultado = slugify(self.anotaciones + "-" + self.calificacion)
        super(Resultados, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.porcentaje_resuelto} {self.fecha_registro_resultado}"

class DetalleContenidoResuleto(models.Model):
    resultado = models.OneToOneField(Resultados, on_delete=models.CASCADE, related_name='detalle')
    # Valor predeterminado se establecerá en el save() del modelo
    fecha_resolver = models.DateField(default=None)  
    puntuacion = models.CharField(max_length=80, blank=False, null=True)

    def save(self, *args, **kwargs):
        if not self.fecha_resolver:
            self.fecha_resolver = self.resultado.fecha_registro_resultado
        super().save(*args, **kwargs)

#MODELO DE REPORTES
class Reportes(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    slug_reporte = models.SlugField(unique=True, blank=True)
    fecha_registro_reporte = models.DateField(auto_now=True)
    usuario_comun = models.ForeignKey(UsuarioComun, on_delete=models.SET_NULL, related_name='reportes', blank=True, null=True)
    contenido_f = models.ForeignKey(Contenido, on_delete=models.SET_NULL, related_name='reportes_contenido', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_reporte = slugify(self.titulo + '-' + self.descripcion)
        super(Reportes, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
#MODELO DE SALA
class Sala(models.Model):
    anotaciones = models.TextField()
    fecha_registro_sala = models.DateField(auto_now=True)
    estado_sala = models.BooleanField(default=True)
    slug_sala = models.SlugField(unique=True, blank=True)
    cancelada_sala = models.BooleanField(default=False)
    usuario_comun = models.ForeignKey(UsuarioComun, on_delete=models.SET_NULL, related_name='salas', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug_sala = slugify(self.anotaciones)
        super(Sala, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.anotaciones} {self.fecha_registro_sala}"

#MODELO DE PETICION
class Peticion(models.Model):
    estado_peticion = models.BooleanField(default=False)
    fecha_registro_peticion = models.DateField(auto_now=True)
    motivo_peticion = models.TextField()
    peticion = models.TextField(max_length=50, blank=True, null=True)
    slug_peticion = models.SlugField(unique=True, blank=True)
    tipo_peticion = models.CharField(max_length=80, blank=False, null=True)
    usuario_comun = models.ForeignKey(UsuarioComun, on_delete=models.CASCADE, related_name='peticiones', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_peticion = slugify(self.motivo_peticion + "-" + self.tipo_peticion)
        super(Peticion, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_peticion} {self.motivo_peticion}"


    
























