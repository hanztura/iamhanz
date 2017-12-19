from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_filer_image.cms_plugins import FilerImagePlugin

from .models import Card
from .forms import CardForm

@plugin_pool.register_plugin
class CardPlugin(FilerImagePlugin):
    cache = False
    form = CardForm
    model = Card
    name = _("Card Plugin")
    render_template = "plugins/card_plugin.html"

    fieldsets = (
        (_('Card'), {
            'fields': [
                'style',
                'card_title',
                'caption_text',
                'image',
                'image_url',
                'alt_text',
            ]
        }),
        (_('Image resizing options'), {
            'fields': (
                'use_original_image',
                ('width', 'height',),
                ('crop', 'upscale',),
                'thumbnail_option',
                'use_autoscale',
            )
        }),
        (None, {
            'fields': ('alignment',)
        }),
        (_('More'), {
            'classes': ('collapse',),
            'fields': (
                'free_link',
                'page_link',
                'file_link',
                ('original_link', 'target_blank',),
                'link_attributes',
                'description',
            ),
        }),
    )