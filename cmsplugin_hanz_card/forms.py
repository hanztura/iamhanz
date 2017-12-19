from cmsplugin_filer_image.forms import FilerImageForm, AttributesWidget

from .models import Card

class CardForm(FilerImageForm):

    class Meta:
        model = Card
        exclude = ['',]

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes']. widget = AttributesWidget()