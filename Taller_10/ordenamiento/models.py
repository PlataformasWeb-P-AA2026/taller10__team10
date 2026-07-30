from django.db import models

class Parroquia(models.Model):
    OPCIONES_UBICACION = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste'),
    ]
    OPCIONES_TIPO = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
    ]

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=20, choices=OPCIONES_UBICACION)
    tipo = models.CharField(max_length=20, choices=OPCIONES_TIPO)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Barrio(models.Model):
    OPCIONES_PARQUES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    ]

    nombre = models.CharField(max_length=100)
    num_viviendas = models.IntegerField('número de viviendas')
    num_parques = models.IntegerField('número de parques', choices=OPCIONES_PARQUES)
    num_edificios = models.IntegerField('número de edificios residenciales')
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    @property
    def datos_presidente(self):
        try:
            return self.presidente
        except Exception:
            return None

    def __str__(self):
        return f"{self.nombre} - {self.parroquia.nombre}"

class Presidente(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=50)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    barrio = models.OneToOneField(Barrio, on_delete=models.CASCADE, related_name='presidente')

    def __str__(self):
        return f"{self.nickname} - {self.profesion}"
