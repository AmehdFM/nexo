from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Clase(models.Model):
    """
    Modelo para representar una clase o curso.
    """
    NIVELES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    
    CATEGORIAS = [
        ('matematicas', 'Matemáticas'),
        ('fisica', 'Física'),
        ('programacion', 'Programación'),
        ('otro', 'Otro'),
    ]
    
    titulo = models.CharField('Título', max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    descripcion_corta = models.CharField('Descripción corta', max_length=300)
    descripcion = models.TextField('Descripción')
    contenido = models.TextField('Contenido')
    imagen = models.ImageField('Imagen', upload_to='clases/', blank=True, null=True)
    categoria = models.CharField('Categoría', max_length=50, choices=CATEGORIAS)
    nivel = models.CharField('Nivel', max_length=50, choices=NIVELES)
    duracion = models.PositiveIntegerField('Duración en horas')
    profesor = models.CharField('Profesor', max_length=100)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    fecha_actualizacion = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        # Generar automáticamente el slug si no existe
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('clases:detalle', args=[self.slug])


class Objetivo(models.Model):
    """
    Objetivos de aprendizaje asociados a una clase.
    """
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='objetivos')
    descripcion = models.CharField('Descripción', max_length=300)
    
    def __str__(self):
        return f"Objetivo de {self.clase.titulo}: {self.descripcion[:30]}..."


class Requisito(models.Model):
    """
    Requisitos previos para tomar una clase.
    """
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='requisitos')
    descripcion = models.CharField('Descripción', max_length=300)
    
    def __str__(self):
        return f"Requisito de {self.clase.titulo}: {self.descripcion[:30]}..."


class Tema(models.Model):
    """
    Temas que componen una clase.
    """
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='temas')
    titulo = models.CharField('Título', max_length=200)
    contenido = models.TextField('Contenido')
    orden = models.PositiveIntegerField('Orden', default=0)
    
    class Meta:
        ordering = ['orden', 'titulo']
    
    def __str__(self):
        return f"{self.clase.titulo} - {self.titulo}"


class Ejercicio(models.Model):
    """
    Ejercicios asociados a una clase.
    """
    DIFICULTAD = [
        ('facil', 'Fácil'),
        ('intermedio', 'Intermedio'),
        ('dificil', 'Difícil'),
    ]
    
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='ejercicios')
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, related_name='ejercicios', null=True, blank=True)
    enunciado = models.TextField('Enunciado')
    imagen = models.ImageField('Imagen', upload_to='ejercicios/', blank=True, null=True)
    solucion = models.TextField('Solución')
    dificultad = models.CharField('Dificultad', max_length=20, choices=DIFICULTAD, default='intermedio')
    
    def __str__(self):
        return f"Ejercicio {self.id} de {self.clase.titulo}"


class Recurso(models.Model):
    """
    Recursos adicionales para una clase.
    """
    TIPOS = [
        ('pdf', 'PDF'),
        ('video', 'Video'),
        ('presentacion', 'Presentación'),
        ('codigo', 'Código'),
        ('otro', 'Otro'),
    ]
    
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='recursos')
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, related_name='recursos', null=True, blank=True)
    titulo = models.CharField('Título', max_length=200)
    descripcion = models.TextField('Descripción', blank=True)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPOS)
    archivo = models.FileField('Archivo', upload_to='recursos/', blank=True, null=True)
    url = models.URLField('URL', blank=True, null=True)
    
    def __str__(self):
        return self.titulo


class Enlace(models.Model):
    """
    Enlaces externos recomendados para una clase.
    """
    TIPOS = [
        ('video', 'Video'),
        ('tutorial', 'Tutorial'),
        ('articulo', 'Artículo'),
        ('curso', 'Curso'),
        ('otro', 'Otro'),
    ]
    
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name='enlaces')
    titulo = models.CharField('Título', max_length=200)
    descripcion = models.TextField('Descripción', blank=True)
    url = models.URLField('URL')
    tipo = models.CharField('Tipo', max_length=20, choices=TIPOS, default='otro')
    
    def __str__(self):
        return self.titulo
        