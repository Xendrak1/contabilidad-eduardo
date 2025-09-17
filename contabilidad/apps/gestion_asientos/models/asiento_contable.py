from django.db import models
class AsientoContable(models.Model):
    class Meta:
        db_table = "asiento_contable"
    
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)