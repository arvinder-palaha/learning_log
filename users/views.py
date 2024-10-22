from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('learning_logs:index')
    template_name = 'registration/logged_out.html'
