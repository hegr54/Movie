from datetime import timedelta,datetime,date
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince
from django.db.models.signals import post_save, pre_save
from .validators import validacion_studio, validacion_studio1
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
    Studio  = models.CharField(max_length=120, validators=[validacion_studio], null=True, blank=True)
    Gender  = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default="draft")
    Slug    = models.SlugField(null=True, blank=True)
    Active  = models.BooleanField(default=True)
    Created = models.DateField(auto_now=True)
    Updated = models.DateField(auto_now=True)
    Timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.Name)

    def save(self, *args, **kwargs):
        print ('Se guardo')
        if not self.Slug:
            if self.Name:
                self.Slug=slugify(self.Name)
        super(Movie,self).save(*args,**kwargs)

def Movie_model_post_seve_receiver(sender, instance, created, *args, **kwargs):
    print ("Se ha almacenado")
    if not instance.Slug and instance.Name:
        instance.Slug=slugify(instance.Name)
        instance.save()

post_save.connect(Movie_model_post_seve_receiver, sender=Movie)

def Movie_model_pre_save_receiver(sender,instance,*args,**kwargs):
    print('Antes de almacenar')
    if not instance.Slug and instance.Name:
        instance.Slug=slugify(instance.Name)
        instance.save()

pre_save.connect(Movie_model_pre_save_receiver, sender=Movie)
