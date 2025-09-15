from django.db import models
class ClaseCuenta(models.Model):
    class Meta:
        # nombre de la tabla 
        # caso contrario se llamaria gestion_cuentas.clase_cuenta
        db_table ="clase_cuenta"
    # nombre con 100 caracteres maximo
    nombre = models.CharField(max_length=100)
    # codigo con valores enteros solo positivos
    codigo = models.PositiveIntegerField()
    # id_padre para la relacion con su padre
    id_padre = models.ForeignKey(
        'self',
        # el padre puede ser null en el caso de la raiz
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="hijos"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre