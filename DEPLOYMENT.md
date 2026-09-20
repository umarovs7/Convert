# PythonAnywhere Deployment Guide (GitHub Clone)

## Bu Django projectni PythonAnywhere'ga GitHub'dan clone qilib yuklash qadamlari:

### 1. PythonAnywhere Hisob Yaratish
- https://www.pythonanywhere.com/ saytiga kirib ro'yxatdan o'ting
- Email manzilingizni tasdiqlang

### 2. Web App Yaratish
- "Web" tabiga o'ting
- "Add a new web app" tugmasini bosing
- "Manual configuration"ni tanlang (tavsiya etiladi)
- Python versiyasini tanlang (3.10 yoki undan yuqori tavsiya etiladi)
- "Next" va "Create" tugmalarini bosing

### 3. GitHub'dan Projectni Clone Qilish
- "Consoles" tabiga o'ting
- "Bash console" tugmasini bosing
- Ishga tushishini kuting
- Quyidagi buyruqlarni yuring:
  ```bash
  cd ~
  git clone https://github.com/umarovs7/Convert.git
  cd Convert
  ```

### 4. Virtual Environment Yaratish
- Bash console ichida:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
  (Prompt boshida (venv) ko'rinadi)

### 5. Dependencies O'rnatish
- Hali Convert papkasida ekanligingiz va venv aktiv ekanligini tekshiring
- Requirements o'rnating:
  ```bash
  pip install -r requirements.txt
  ```
- WeasyPrint uchun GTK+ libraries kerak. PythonAnywhere'da ular allaqachon o'rnatilgan.

### 6. Web App Konfiguratsiyasi
- "Web" tabga o'ting
- "Code" bo'limiga tushing
- Quyidagilarni belgilang:
  - **Working directory**: `/home/loveconvert/Convert`
  - **Virtualenv**: `/home/loveconvert/Convert/venv`
  - **WSGI configuration file**: `/home/loveconvert/Convert/convert/wsgi.py`
- Pastki qismidagi "Save" tugmasini bosing

### 7. Environment Variables Sozlash
- "Web" tabda, "Environment variables" bo'limiga tushing
- "Add variable" tugmasini bosing
- **Key**: `SECRET_KEY`
- **Value**: Bash console'da quyidagi buyruq bilan random key yarating:
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- Natijani nusxalab value sifatida qo'ying
- "OK" va keyin "Save" tugmalarini bosing

### 8. Static Files Konfiguratsiyasi
- "Web" tabda, "Static files" bo'limiga tushing
- "Enter a new static files URL" tugmasini bosing
  - **URL**: `/static/`
  - **Directory**: `/home/loveconvert/Convert/staticfiles`
- "Save" tugmasini bosing
- Bash consolega qaytib quyidagini yuring:
  ```bash
  python manage.py collectstatic
  ```
- So'ralganda `yes` deb yozing

### 9. Media Files Konfiguratsiyasi
- "Web" tabda, "Static files" bo'limiga tushing
- "Enter a new static files URL" tugmasini bosing
  - **URL**: `/media/`
  - **Directory**: `/home/loveconvert/Convert/media`
- "Save" tugmasini bosing

### 10. Database Sozlash
- Bash console'da quyidagini yuring:
  ```bash
  python manage.py migrate
  ```
- Bu database jadvallarini yaratadi

### 11. ALLOWED_HOSTS Yangilash
- settings.py allaqachon sozlangan (DEBUG=False, ALLOWED_HOSTS=['loveconvert.pythonanywhere.com'])
- Agar o'zgartirish kerak bo'lsa:
  ```bash
  nano convert/settings.py
  ```
- `Ctrl+X`, keyin `Y`, keyin `Enter` bosish orqali saqlang va chiqing

### 12. Web Appni Reload Qilish
- "Web" tabga o'ting
- Yuqoridagi katta yashil "Reload" tugmasini bosing
- Reload bo'lishini kuting (taxminan 10-20 soniya)

### 13. Saytni Test Qilish
- Saytingiz linkiga bosing (masalan, http://loveconvert.pythonanywhere.com)
- Django app endi ishga tushdi!

## Muhim Eslatmalar:
- Project card yaratish uchun WeasyPrint ishlatadi. Bu PythonAnywhere'da maxsus sozlashsiz ishlaydi.
- Developmentda (Windows), card generation ishlamasligi mumkin (GTK+ libraries yo'q), lekin app friendly error message ko'rsatadi.
- PythonAnywhere'da card generation mukammal ishlaydi.
- SQLite database ishlatiladi (kichik projectlar uchun mos).
- DEBUG production uchun False qilingan.
