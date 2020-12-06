from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.conf import settings


class indexTemplateView(LoginRequiredMixin, TemplateView):
    '''
    View used to render the index.html template.
    '''
    def get_template_names(self):
        if settings.DEBUG:
            template_name = "index-dev.html"
        else:
            template_name = "index.html"
        return template_name
