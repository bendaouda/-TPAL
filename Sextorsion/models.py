from django.db import models

# Create your models here.
class Sextorsion(models.Model):
    titre=models.CharField(max_length=200,null=True)
    contenu=models.TextField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    date_modification = models.DateTimeField(auto_now=True)
    image = models.ImageField()


    def __str__(self):
        return self.titre