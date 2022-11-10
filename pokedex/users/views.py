from django.contrib import messages
from django.shortcuts import (
    redirect,
    render,
)

from .forms import UserRegisterForm


def create_new_user(form, request):
    form.save()
    username = form.cleaned_data.get("username")
    success_message = f"Account created for {username}. please login"
    messages.success(request, success_message)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            create_new_user(form, request)
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, template_name="users/register.html", context=context)
