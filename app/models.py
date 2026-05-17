from django.db import models

# Create your models here.






from django.db import models
from django.urls import reverse
from django.utils import timezone

class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Projet(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    long_description = models.TextField(blank=True, help_text="Detailed description for the project page")
    image = models.ImageField(upload_to='projets/', help_text="Main image for the project")
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)  # Technologies utilisées
    date_created = models.DateField(default=timezone.now)

    # Metadata
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-date_created']
    
    # Methods
    def __str__(self):
        return self.name

class ProjetImage(models.Model):
    projet = models.ForeignKey(Projet, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projets/illustrations/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.projet.name}"
   
class Certifications(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    date_obtained = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True)

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['-date_obtained']

    def __str__(self):
        return f"{self.name} - {self.source}"
    


class Experience(models.Model):
    titre_poste =models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.titre_poste




class Formation(models.Model):
    titre_formation = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)



    def __str__(self):
        return self.titre_formation




class Contact(models.Model):
    nom =models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField() 
        
    def __str__(self):
        return self.nom


class Cv(models.Model):
    cv_file =models.FileField(upload_to='CV/', blank=True, null=True)

    def __str__(self):
        return self.cv_file.name


