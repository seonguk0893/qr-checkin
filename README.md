# 무인매장 출입 QR 발급 시스템

이 프로젝트는 무인매장에 입장하기 전 회원가입 및 로그인 절차를 통해 출입 QR 코드를 발급받는 Django 기반의 웹 애플리케이션입니다. 회원가입을 통해 QR 코드가 생성되며, 로그인 시 QR 코드를 확인할 수 있는 페이지로 이동됩니다.

</br>

## 주요 기능

- **회원가입**: 사용자 정보를 입력하여 계정을 생성하고, QR 코드를 발급받습니다.
- **로그인**: 등록된 계정으로 로그인하면 자신의 QR 코드를 확인할 수 있습니다.
- **QR 코드 발급**: 회원가입 완료 시 고유 QR 코드가 발급되며, 이를 통해 무인매장 출입이 가능합니다.
- **QR 코드 보기**: 로그인 후 QR 코드 확인 페이지로 이동하여 QR 코드를 확인할 수 있습니다.
- **AWS S3 연동**: QR 코드 이미지는 AWS S3에 저장됩니다.

</br>

## 기술 스택
![py](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![django](https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=django&logoColor=white)
![html](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white) 
![css](https://img.shields.io/badge/CSS-00758F?&style=for-the-badge&logo=css3&logoColor=white) 
![js](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white)
![mysql](https://img.shields.io/badge/Mysql-F29111?style=for-the-badge&logo=mysql&logoColor=white)

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: MySQL
- **File Storage**: AWS S3
- **배포**: AWS를 통한 배포 (선택 사항)

</br>

## 설치 및 실행 방법

1. **프로젝트 클론**
    ```bash
    git clone https://github.com/cookiesthatimade/QR_checkin.git
    cd QR_checkin
    ```

2. **필수 패키지 설치**
    ```bash
    pip install -r requirements.txt
    ```

3. **Django 설정 파일 설정**
    `settings.py` 파일에 AWS S3 설정 및 데이터베이스 설정을 적용합니다.

4. **데이터베이스 마이그레이션**
    ```bash
    python manage.py migrate
    ```

5. **서버 실행**
    ```bash
    python manage.py runserver
    ```

6. **프로젝트 접속**
    브라우저에서 `http://127.0.0.1:8000`으로 접속하여 프로젝트를 확인할 수 있습니다.

</br>

## 사용 예시

1. 회원가입 페이지에서 필요한 정보를 입력하고 계정을 생성합니다.
2. 로그인 후 발급된 QR 코드를 확인할 수 있습니다.
3. QR 코드를 무인매장 출입 시 스캔하여 인증할 수 있습니다.

</br>

## AWS S3 설정 방법

1. AWS 콘솔에서 S3 버킷을 생성합니다.
2. 생성한 S3 버킷 정보를 manage.py와 동일 선상에 `my_settings.py`에 추가합니다.
    ```python
    AWS_ACCESS_KEY_ID = 'your_access_key'
    AWS_SECRET_ACCESS_KEY = 'your_secret_key'
    AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    AWS_REGION = 'your_region'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_REGION)
    ```
</br>

## MySQL DB 설정 방법

1. MySQL DB를 생성합니다.
2. 생성한 DB 정보를 `my_settings.py`에 추가합니다.
    ```python
    DATABASES = {
      'default' : {
          'ENGINE' : 'django.db.backends.mysql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'your_db_host',
          'PORT': 'your_db_port',
    ```
</br>

## QR 발급 API_KEY 추가

*해당 프로젝트는 타 사의 QR 발급 API를 이용하였습니다.
1. `my_settings.py`에 API_KEY 추가
  ```python
  SECRET_KEY = 'your_api_key'
  ```
    
</br>

## 기여 방법

1. 이 프로젝트를 포크합니다.
2. 새로운 브랜치를 만듭니다. (`git checkout -b feature/새로운기능`)
3. 변경 사항을 커밋합니다. (`git commit -am 'Add 새로운 기능'`)
4. 브랜치에 푸시합니다. (`git push origin feature/새로운기능`)
5. 풀 리퀘스트를 생성합니다.

</br>

## 페이지 설명

### 로그인 페이지
  - biostar API(002.update) 를 통해 출입 QR의 유효 시간 재 설정
  - ID 와 P/W 불일치 시 에러 모달 구현

<img width="500" alt="Untitled" src="https://github.com/user-attachments/assets/b4132a8a-cc5e-4860-9a7f-d32c99477700">
<img width="500" alt="Untitled1" src="https://github.com/user-attachments/assets/6b5c13ac-0f76-4bef-bfcf-4178d9d016f2">


### 회원가입 페이지
  - biostar API(001.create) 를 통해 사용자의 출입 QR 생성
  - ID,Email 입력 모달 구현
  - P/W 와 P/W Confirm 불일치 시 모달 구현
  - 모든 정보 불입력 시 모달 구현
  - 회원 가입 완료 모달 구현

<img width="500" alt="Untitled2" src="https://github.com/user-attachments/assets/6a00ee61-ae13-49b0-81d5-d260c0251d27">
<img width="500" alt="Untitled3" src="https://github.com/user-attachments/assets/f9bd6fc9-e68a-42bf-8b97-61d6930dd969">


### 로그인 후 출입QR 페이지


<img width="500" alt="image4" src="https://github.com/user-attachments/assets/ca93e143-974c-49fd-bc83-2f26fa3ab2e0">

