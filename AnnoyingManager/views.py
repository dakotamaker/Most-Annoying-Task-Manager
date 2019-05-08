from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from . import forms
from . import models


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'main/login.html', {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        if models.User.objects.filter(email=email).exists():
            if models.User.objects.filter(email=email, password=password).exists():
                request.session["email"] = email
                return redirect(r'/tasks')
            else:
                error = "Your password is incorrect. Please try again."
        else:
            error = "That use does not exist. Please register."
        return render(request, 'main/login.html', {"form": form, "error": error})


class Register(View):
    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'main/register.html', {"form": form})

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        email = request.POST.get("email")
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        if form.is_valid() and phone_number != '' and user_name != '' and password != '':
            u = models.User(email=email, user_name=user_name, password=password, phone_number=phone_number)
            u.save()
            return redirect(r'/login')
        else:
            error = 'Form is not valid. Please try again.'
            return render(request, 'main/register.html', {"form": form, "error": error})


class TaskList(View):
    def get(self, request):
        email = request.session.get("email")
        u = models.User.objects.filter(email=email)
        valid_user = False
        tasks = []
        if u.exists():
            u = models.User.objects.get(email=email)
            valid_user = True
            tasks = list(models.Task.objects.filter(user=u))
        return render(request, 'main/taskList.html', {"valid_user": valid_user, "tasks": tasks, "user":u})

    def post(self, request):
        email = request.session.get("email")
        u = models.User.objects.filter(email=email)
        valid_user = False
        resultMessage = ""
        tasks = []
        if u.exists():
            u = models.User.objects.get(email=email)
            valid_user = True
            u = models.User.objects.get(email=email)
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            done = request.POST.get("done") == 'on' and True or False
            try:
                t = models.Task(done=done, description=description, user=u,
                                due_date=int(datetime.fromisoformat(due_date).timestamp()))
                t.save()
            except ValueError:
                resultMessage = "There is an error in your values you entered. Please try again."

            tasks = list(models.Task.objects.filter(user=u))
        return render(request, 'main/taskList.html', {"valid_user": valid_user, "tasks": tasks, "resultMessage": resultMessage, "user":u})


class Profile(View):
    def get(self, request):
        email = request.session.get("email")
        u = models.User.objects.filter(email=email)
        form = forms.UserProfileForm()
        valid_user = False
        if u.exists():
            u = models.User.objects.get(email=email)
            valid_user = True
            form.initial['user_name'] = u.user_name
            form.initial['email'] = u.email
            form.initial['phone_number'] = u.phone_number
        return render(request, 'main/userProfile.html', {"valid_user": valid_user, "user": u, "form": form})

    def post(self, request):
        email = request.session.get("email")
        u = models.User.objects.filter(email=email)
        form = forms.UserProfileForm(request.POST)
        valid_user = False
        resultMessage = ""
        if u.exists():
            u = models.User.objects.get(email=email)
            valid_user = True
            u.user_name = request.POST.get("user_name")
            u.email = request.POST.get("email")
            u.phone_number = request.POST.get("phone_number")

            if len(list(models.User.objects.filter(email=u.email).exclude(user_id=u.user_id))) > 0:
                resultMessage = "This email is already being used, please try again."
            elif len(list(models.User.objects.filter(phone_number=u.phone_number).exclude(user_id=u.user_id))) > 0:
                resultMessage = "This phone number is already being used, please try again."
            else:
                resultMessage = "Saved!"
                u.save()
                request.session["email"] = u.email
        return render(request, 'main/userProfile.html', {"valid_user": valid_user, "user": u | None, "form": form, "resultMessage": resultMessage})


class Logout(View):
    def get(self, request):
        request.session["email"] = ""
        return redirect(r'/login')


class LateTasks(View):
    def get(self, request):
        email = request.session.get("email")
        u = models.User.objects.filter(email=email)
        time = int(datetime.now().timestamp())
        late_tasks = []
        valid_user = False
        if u.exists():
            u = models.User.objects.get(email=email)
            valid_user = True
            tasks = list(models.Task.objects.filter(user=u))
            for task in tasks:
                if task.due_date < time:
                    late_tasks.append(task)
        return render(request, 'main/lateTasks.html', {"valid_user": valid_user, "late_tasks": late_tasks})


def delete_task(request, task_id=None):
    email = request.session.get("email")
    u = models.User.objects.filter(email=email)
    if u.exists():
        u = models.User.objects.get(email=email)
        task = models.Task.objects.get(task_id=task_id, u=u)
        task.delete()
        return redirect(r'/tasks')
    return redirect(r'/login')


def delete_user(request, user_id=None):
    email = request.session.get("email")
    u = models.User.objects.filter(email=email)
    if u.exists():
        u = models.User.objects.get(email=email)
        if u == models.User.objects.get(user_id=user_id):
            request.session["email"] = ""
            u.delete()
    return redirect(r'/login')
