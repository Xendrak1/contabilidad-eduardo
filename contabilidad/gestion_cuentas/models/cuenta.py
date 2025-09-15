from django.db import models
from .clase_cuenta import ClaseCuenta

class Cuenta(models.Model):
    
    class Meta:
        # para definir el nombre de la tabla
        # caso contrario seria gestios_cuenta.cuenta 
        db_table = "cuenta"
    # codigo con tipo int solo valeres positivos    
    codigo = models.PositiveBigIntegerField()
    # nombre con maximo de 100 caracteres
    nombre = models.CharField(max_length=100)
    # estado booleano 
    estado = models.BooleanField(null=True)
    # relacion con la clase de cuenta
    id_clase_cuenta = models.ForeignKey(
        ClaseCuenta,
        # si se eliminar la clase cuenta no se elimina esta cuenta
        on_delete=models.SET_NULL,
        blank=True,null=True,
        related_name="grupo"
        
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    