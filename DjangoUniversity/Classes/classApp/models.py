from django.db import models



class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False) #charField is used for small str types
    course_number = models.IntegerField(default=0)
    instructor = models.CharField(max_length=60, default='', blank=True)
    duration = models.FloatField(default=0.0)

    objects = models.Manager()

    def __str__(self):
        return self.title
# Create your models here.
