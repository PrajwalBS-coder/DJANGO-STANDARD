from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator,MaxValueValidator
import uuid
from django.utils.translation import gettext_lazy as _

gender_choices=[
    ('M', 'Male'),
    ('F', 'female'),
    ('O', 'Others')
]

Roles = [
    ('Dev', 'Developer'),
    ('PM', 'Project Manager'),
    ('QA', 'Quality Analyst'),
    ('UX', 'UI/UX Designer')
]


class Employee(models.Model):
    id = models.UUIDField(_('ID'),db_column='id',default=uuid.uuid4,editable=False ,primary_key=True)
    name = models.CharField(max_length=100)
    email =models.EmailField(unique=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(50)])
    gender = models.CharField(choices= gender_choices,max_length=1)
    salary = models.DecimalField(max_digits=10,decimal_places=3,validators=[MinValueValidator(10000)])
    date_joined = models.DateField(default=now)
    is_active  = models.BooleanField(default= True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_joined']
        verbose_name = _('Employee')
        verbose_name_plural = _('Employee')