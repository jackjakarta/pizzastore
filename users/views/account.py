from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegisterForm


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully!")
            return redirect("home")

    return render(request, "users/register.html", {
        "form": form
    })
