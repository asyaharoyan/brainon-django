from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    """
    Render home page
    """
    template_name = 'home/index.html'