from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    age = models.IntegerField()

    def __repr__(self) -> str:
        return f'Nombre: {self.first_name} {self.last_name}, Edad: {self.age}'
