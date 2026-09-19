# PythonAnywhere Deployment Guide (GitHub Clone)

## Steps to deploy this Django project to PythonAnywhere using GitHub:

### 1. Create a PythonAnywhere Account
- Sign up at https://www.pythonanywhere.com/
- Verify your email address

### 2. Create a Web App
- Go to the "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration" (recommended)
- Select Python version (3.10 or higher recommended)
- Click "Next" and "Create"

### 3. Clone Your Project from GitHub
- Go to the "Consoles" tab
- Click "Bash console"
- Wait for it to start
- Run these commands:
  ```bash
  cd ~
  git clone https://github.com/umarovs7/Convert.git
  cd Convert
  ```
  (Replace YOUR_USERNAME with your actual GitHub username)

### 4. Create Virtual Environment
- In the same Bash console:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
  (You should see (venv) at the beginning of your prompt)

### 5. Install Dependencies
- Make sure you're still in the Convert folder and venv is activated
- Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
- WeasyPrint requires GTK+ libraries. On PythonAnywhere, these are already installed.

### 6. Configure the Web App
- Go to the "Web" tab
- Scroll down to "Code" section
- Set:
  - **Working directory**: `/home/loveconvert/Convert`
  - **Virtualenv**: `/home/loveconvert/Convert/venv`
  - **WSGI configuration file**: `/home/loveconvert/Convert/convert/wsgi.py`
- Click "Save" at the bottom

### 7. Set Environment Variables
- In the "Web" tab, scroll to "Environment variables" section
- Click "Add variable"
- **Key**: `SECRET_KEY`
- **Value**: Generate a random key using this command in Bash:
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- Copy the output and paste it as the value
- Click "OK" and then "Save"

### 8. Configure Static Files
- In the "Web" tab, scroll to "Static files" section
- Click "Enter a new static files URL"
  - **URL**: `/static/`
  - **Directory**: `/home/loveconvert/Convert/staticfiles`
- Click "Save"
- Go back to Bash console and run:
  ```bash
  python manage.py collectstatic
  ```
- Type `yes` when prompted

### 9. Configure Media Files
- In the "Web" tab, scroll to "Static files" section
- Click "Enter a new static files URL"
- **URL**: `/media/`
- **Directory**: `/home/loveconvert/Convert/media`
- Click "Save"

### 10. Set Up Database
- In Bash console, run:
  ```bash
  python manage.py migrate
  ```
- This will create the database tables

### 11. Update ALLOWED_HOSTS
- In Bash console, edit settings.py:
  ```bash
  nano convert/settings.py
  ```
- Find `ALLOWED_HOSTS = ['*']`
- Change it to your PythonAnywhere domain:
  ```python
  ALLOWED_HOSTS = ['loveconvert.pythonanywhere.com']
  ```
- Press `Ctrl+X`, then `Y`, then `Enter` to save and exit

### 12. Reload the Web App
- Go to the "Web" tab
- Click the big green "Reload" button at the top
- Wait for it to reload (about 10-20 seconds)

### 13. Test Your Site
- Click the link to your site (e.g., http://loveconvert.pythonanywhere.com)
- Your Django app should now be live!

## Important Notes:
- The project uses WeasyPrint for generating card images. This works on PythonAnywhere without special setup.
- In development (Windows), card generation may not work due to missing GTK+ libraries, but the app will show a friendly error message.
- On PythonAnywhere, card generation will work perfectly.
- SQLite is used as the database (suitable for small projects).
- DEBUG is set to False for production.
