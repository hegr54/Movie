from django.db import models

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
