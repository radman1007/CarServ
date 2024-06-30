from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)