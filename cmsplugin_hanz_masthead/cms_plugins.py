from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_filer_image import cms_plugins

from .models import Masthead
from .forms import MastheadImageForm

@plugin_pool.register_plugin
class MastheadPlugin(cms_plugins.FilerImagePlugin):
    form = MastheadImageForm
    model = Masthead
    name = _("Masthead Plugin")
    
    render_template = "plugins/masthead_plugin.html"

    fieldsets = (
        (_('Masthead'), {
            'fields': [
                'masthead_name',
                'masthead_title',
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
    
    allow_children = False
    cache = False