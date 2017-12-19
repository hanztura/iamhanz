from cmsplugin_filer_image import forms as _forms

from .models import Masthead


class MastheadImageForm(_forms.FilerImageForm):

    class Meta:
        model = Masthead
        exclude = ['style']

    def __init__(self, *args, **kwargs):
        super(MastheadImageForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = _forms.AttributesWidget()
