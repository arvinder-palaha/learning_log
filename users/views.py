from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django_ratelimit.decorators import ratelimit

# @ratelimit(key='ip', rate='5/m', method=['POST', 'GET'], block=True)
# def register(request):
#     return HttpResponseNotFound("Registration is disabled")
#     if request.method != 'POST':
#         form = UserCreationForm()
#     else:
#         form = UserCreationForm(data=request.POST)

#         if form.is_valid():
#             new_user = form.save()
#             login(request, new_user)
#             return redirect('learning_logs:index')

#     context = {'form': form}
#     return render(request, 'registration/register.html', context)
