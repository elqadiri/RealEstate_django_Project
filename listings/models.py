from django.db import models

# Create your models here.

class Listings(models.Model):
    type_bien = models.CharField(max_length=150, default='app/villa...')
    Action_commerciale = models.CharField(max_length=150, default='vendre')
    Titre = models.CharField(max_length=150, default='title')
    Prix = models.FloatField()
    Surface = models.IntegerField()
    Adresse = models.CharField(max_length=150)
    Nombre_chambre = models.IntegerField()
    Nombre_salle_bain = models.IntegerField()

    def __str__(self):
        return self.type_bien

class ListingImage(models.Model):
    listing = models.ForeignKey(Listings, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.listing.Titre}"

class ContactMessage(models.Model):
    name= models.CharField(max_length=100,default='name')
    email = models.CharField(max_length=100, default='email')
    subject = models.CharField(max_length=150, default='subject')
    message = models.CharField(max_length=500,default='message')
    def __str__(self):
        return f"{self.name} - {self.subject}"