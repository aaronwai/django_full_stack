from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel

User = get_user_model()

class Apartment(TimeStampedModel):
    unit_number = models.CharField(max_length=10, verbose_name=_("Unit Number"))
    floor = models.PositiveIntegerField(verbose_name=_("Floor")) 
    building = models.CharField(max_length=50, verbose_name=_("Building"))
    tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="apartments", verbose_name=_("Tenant"))
    def __str__(self)->str:
        return f"Unit: {self.unit_number} - Floor: {self.floor} - Building: {self.building}"