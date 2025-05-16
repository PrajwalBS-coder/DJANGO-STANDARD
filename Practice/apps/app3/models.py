from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=100,
                            null=True,
                            blank=True,
                            db_column="Name of File",
                            db_comment='image name')
    file = models.FileField(upload_to='images/',
                            null=True,
                            blank=True,
                            verbose_name='Image Files')
    def __str__(self):
        return self.name