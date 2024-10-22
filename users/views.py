from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('learning_logs:index')
    template_name = 'registration/logged_out.html'

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
