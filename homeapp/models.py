from django.db import models

# Create your models here.
#"3050755494"
class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    subscibed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
