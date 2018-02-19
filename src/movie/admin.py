from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieModelAdmin(admin.ModelAdmin):
    fields=[
         'Name',
         'Year',
         'Studio',
         'Gender',
         'Slug',
         'Active',
         'publish_date',
         # 'Created',
         'Updated',
         'Timestamp',
         'get_age'
         #'new_contect',

     ]
    readonly_fields=['Updated','Timestamp','get_age']

    # def new_contect(self,obj,*args,**kwargs):
    #     return str(obj.Name)

    def get_age(self,obj,*args,**kwargs):
        return str(obj.age)

    class Meta:
        model=Movie

admin.site.register(Movie,MovieModelAdmin)
