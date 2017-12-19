from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

# Create your models here.
class Navbar(CMSPlugin):


    class Meta:
        verbose_name='Navigation Bar'
        verbose_name_plural='Navigation Bars'


    brand = models.CharField(max_length=10)
    link1 = models.URLField(max_length=10, null=True, blank=True)
    link2 = models.CharField(max_length=10, null=True, blank=True)
    link3 = models.CharField(max_length=10, null=True, blank=True)
    link4 = models.CharField(max_length=10, null=True, blank=True)
    link5 = models.CharField(max_length=10, null=True, blank=True)
    link6 = models.CharField(max_length=10, null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Make sure that either image or image_url is set
        if (not self.brand):
            raise ValidationError(_('Either an image or an image url must be selected.'))