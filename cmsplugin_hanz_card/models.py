from django.db import models


from cmsplugin_filer_image.models import FilerImage

# Create your models here.
class Card(FilerImage):
    card_title = models.CharField(max_length=30)