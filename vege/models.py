
from django.db.models import Model,FileField

# Create your models here.

class pdf1(Model):
    receipe_image = FileField(upload_to='pdf_fol')

    # def __str__(self) -> str:
    #     return self.receipe_name



