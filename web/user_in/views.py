from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, AuthenticationFormWithPlaceholders
from django.views.decorators.csrf import csrf_protect
import requests
from datetime import datetime
import os
from django.conf import settings
import time
from .models import CustomUser
import qrcode

API_URL_REGISTER = 'http://3.34.221.229:80/InterFace.asmx/IF_SUNNYFACTORY_001'
API_URL_UPDATE = 'http://3.34.221.229:80/InterFace.asmx/IF_SUNNYFACTORY_002'
API_KEY = '9PPUf6mXnd9DGQItcRU+ppQLUyMFz0oF'
HEADERS = {'x-api-key': API_KEY}


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
                # 사용자 정보 업데이트 API 호출
                return update_user_view(request)
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

            # 외부 API에 사용자 정보 등록
            now = time.strftime('%Y-%m-%d')
            data = {
                "user_id": user.id,
                "user_name": user.name,
                "hp_no": user.contact,
                "qrcode_val": user.id,
                "start_dtm": now+" 00:00:00",
                "end_dtm": now+" 23:00:00",
                "user_email": user.email
            }

            # URL 및 헤더 설정
            API_URL_REGISTER = 'http://3.34.221.229:80/InterFace.asmx/IF_SUNNYFACTORY_001'
            HEADERS = {'x-api-key': '9PPUf6mXnd9DGQItcRU+ppQLUyMFz0oF'}

            response = requests.post(
                API_URL_REGISTER, json=data, headers=HEADERS)

            # QR 코드 생성
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data['qrcode_val'])
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')

            # QR 코드 이미지 파일 저장
            qrcodes_dir = os.path.join(settings.STATIC_ROOT, 'qrcodes')
            if not os.path.exists(qrcodes_dir):
                os.makedirs(qrcodes_dir)
            img_path = os.path.join(qrcodes_dir, f'{user.id}.png')
            img.save(img_path)

            # QR 코드 이미지 경로를 사용자 모델에 저장
            user.qr_code_path = img_path
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


@csrf_protect
def update_user_view(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        now = time.strftime('%Y-%m-%d')

        data = {
            "user_id": user.id,
            "user_name": user.name,
            "hp_no": user.contact,
            "user_email": user.email,
            "start_dtm": now+" 00:00:00",
            "end_dtm": now+" 23:00:00",
            "edit_yn": "N"
        }

        API_URL_UPDATE = 'http://3.34.221.229:80/InterFace.asmx/IF_SUNNYFACTORY_002'
        headers = {'x-api-key': '9PPUf6mXnd9DGQItcRU+ppQLUyMFz0oF'}

        response = requests.post(API_URL_UPDATE, json=data, headers=HEADERS)
        response.text[response.text.find('result_msg'):]
        print("Status:", response.text)
        return redirect('/home')
    return render(request, 'user_in/update.html')
