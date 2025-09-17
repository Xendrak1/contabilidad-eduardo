from django.db import models
from ...gestion_cuentas.models.cuenta import Cuenta
from .asiento_contable import AsientoContable
class Movimiento(models.Model):
    class Meta:
        db_table = "movimiento"
    
    referencia = models.CharField(max_length=200)
    debe = models.DecimalField(max_digits=10,decimal_places=3)
    haber = models.DecimalField(max_digits=10,decimal_places=3)
    id_cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name="movimientos"
    )
    id_asiento_contable = models.ForeignKey(
        AsientoContable,
        on_delete=models.CASCADE,
        related_name="movimientos"
    )