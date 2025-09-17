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
    estado = models.BooleanField(default=True)
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
    
    def save(self, *args, **kwargs):
        if not self.id_clase_cuenta:
            codigo_str = str(self.codigo)
            
            # Buscar la ClaseCuenta cuyo código sea prefijo del código de la cuenta
            clase = ClaseCuenta.objects.filter(
                codigo__in=[int(codigo_str[:i+1]) for i in range(len(codigo_str))]
            ).order_by('-codigo').first()  # Tomar la más específica
            
            self.id_clase_cuenta = clase  # Puede ser None si no encuentra ninguna

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    