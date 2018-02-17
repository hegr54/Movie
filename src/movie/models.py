from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, pre_save
# Create your models here.
PUBLISH_CHOICES=(
    ('draft','Draft'),
    ('publish','Publish'),
    ('publich','publich'),
    ('private','Private')
    )
class Movie(models.Model):
    Name    = models.CharField(max_length=250,
                                    verbose_name='Movie Name',
                                    unique=True,
                                    error_messages={
                                    "unique": "Este titulo no es unico, intenta de nuevo."
                                    },
                                    help_text='debe ser un titulo unico.')
    Year    = models.CharField(max_length=120)
    Studio  = models.CharField(max_length=120,  null=True, blank=True)
    Gender  = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default="draft")
    Slug    = models.SlugField(null=True, blank=True)
    Active  = models.BooleanField(default=True)
    Created = models.DateField(auto_now=True)
    Updated = models.DateField(auto_now=True)
    Timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return smart_text(self.Name)

    def save(self, *args, **kwargs):
        print ('Se guardo')
        if not self.slug:
            if self.Name:
                self.slug=slugify(self.Name)
        super(Movie,self).save(*args,**kwargs)

def Movie_model_post_seve_receiver(sender, instance, created, *args, **kwargs):
    print ("Se ha almacenado")
    if not instance.slug and instance.Name:
        instance.slug=slugify(instance.Name)
        instance.save()

post_save.connect(Movie_model_post_seve_receiver, sender=Movie)

def Movie_model_pre_save_receiver(sender,instance,*args,**kwargs):
    print('Antes de almacenar')
    if not instance.slug and instance.Name:
        instance.slug=slugify(instance.Name)
        instance.save()

pre_save.connect(Movie_model_pre_save_receiver, sender=Movie)
