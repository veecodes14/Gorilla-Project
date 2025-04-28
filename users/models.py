from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date
from PIL import Image

class Waitlist(models.Model):
    name = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 200, unique=True)
    dob = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f'{self.name} Profile'
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.dob:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            if age < 18:
                raise ValidationError("You must be at least 18 years old to register.")


