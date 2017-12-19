from django.db import models
from django.utils.translation import ugettext_lazy as _

from cmsplugin_filer_image.models import FilerImage

# Create your models here.
class Masthead(FilerImage):
    masthead_name = models.CharField(("name"), max_length=50)
    masthead_title = models.CharField( max_length=50)