from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # 追加
from django.views.generic import DetailView # 追加



# ========以下を追記========
from django.http import HttpResponse


def index(request):
    return render(request, "kanban/index.html")

@login_required
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'kanban/signup.html', context)


class UserDetailView(DetailView):
    model = User
    template_name = "kanban/users/detail.html"
