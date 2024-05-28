from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, AuthenticationFormWithPlaceholders
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    return render(request, 'user_in/index.html')


@csrf_protect
def home(request):
    if request.user.is_authenticated:
        return render(request, 'user_in/home.html')
    else:
        return redirect('index')


@never_cache
@csrf_protect
def logout_view(request):
    if request.method == 'POST':
        request.session.flush()
        response = redirect('/index')
        return response
    else:
        return render(request, 'user_in/home.html')


@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = AuthenticationFormWithPlaceholders(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                messages.error(request, "ID 또는 P/W가 잘못되었습니다.")
        else:
            messages.error(request, "ID 또는 P/W가 잘못되었습니다.")
    else:
        form = AuthenticationFormWithPlaceholders()
    return render(request=request, template_name="user_in/index.html", context={"login_form": form})


@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.name = form.cleaned_data.get('name')
            user.contact = form.cleaned_data.get('contact')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, "회원가입이 완료되었습니다.")
            return redirect('/')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            login_form = AuthenticationFormWithPlaceholders()
            return render(request, 'user_in/index.html', {'form': form, 'login_form': login_form})
    else:
        form = SignUpForm()
        login_form = AuthenticationFormWithPlaceholders()
    return render(request, 'user_in/index.html', {'form': form, 'login_form': login_form})
