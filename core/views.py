from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tittle':'Directorio Médico'})
        

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

#def home(request):
    #return render(request, "core/home.html")

#def sample(request):
    #return render(request, "core/sample.html")