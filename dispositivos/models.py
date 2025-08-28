from django.db import models

# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, default="Sin descripcion")

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, default="Sin descripcion")

    def __str__(self):
        return self.nombre
    
class Dispositivo(models.Model):
    nombre_dispositivo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='dispositivos', default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='dispositivos', default=1)
    
    def __str__(self):
        return f"{self.nombre_dispositivo}, {self.marca}, {self.modelo}"

class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='mediciones')
    fecha = models.DateField()
    hora = models.TimeField()
    consumo = models.FloatField()

    def __str__(self):
        return f"{self.fecha}, {self.hora}, {self.consumo}"

class Alerta(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='alertas')
    valor_medido = models.FloatField()
    tipo_alerta = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo_alerta}, {self.valor_medido}"
