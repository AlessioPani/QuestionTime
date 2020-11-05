from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class indexTemplateView(TemplateView, LoginRequiredMixin):
    '''
    View used to render the index.html template.
    '''
    def get_template_names(self):
        template_name = "index.html"
        return template_name