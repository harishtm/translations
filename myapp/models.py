from django.db import models
from django.utils.translation import ugettext_lazy as _
import vinaigrette


# Create your models here.

class Register(models.Model):
    first_name = models.CharField(_('First Name') , max_length=100)
    last_name = models.CharField(_('Last Name') , max_length=100)
    emp_id = models.CharField(_('Emp Id') , max_length=10)

    def __unicode__(self):
        return self.first_name

vinaigrette.register(Register, ['first_name', 'last_name'])


