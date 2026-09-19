# PythonAnywhere Deployment Guide

## Steps to deploy this Django project to PythonAnywhere:

### 1. Create a PythonAnywhere Account
- Sign up at https://www.pythonanywhere.com/

### 2. Create a Web App
- Go to the "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration" (recommended)
- Select Python version (3.10 or higher)

### 3. Upload Your Code
- Use the "Files" tab to upload your project files
- Or use git: `git clone <your-repo-url>` in the Bash console

### 4. Install Dependencies
- In the Bash console, navigate to your project folder
- Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
- Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
- WeasyPrint requires GTK+ libraries. On PythonAnywhere, these are already installed.

### 5. Configure the Web App
- In the "Web" tab, set:
  - **Working directory**: `/home/yourusername/Convert`
  - **Virtualenv**: `/home/yourusername/Convert/venv`
  - **WSGI configuration file**: `/home/yourusername/Convert/convert/wsgi.py`

### 6. Set Environment Variables
- In the "Web" tab, go to "Variables" section
- Add `SECRET_KEY` with a random secure key (generate using: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)

### 7. Configure Static Files
- In the "Web" tab, go to "Static files" section
- Add:
  - **URL**: `/static/`
  - **Directory**: `/home/yourusername/Convert/staticfiles`
- Run collectstatic:
  ```bash
  python manage.py collectstatic
  ```

### 8. Configure Media Files
- In the "Web" tab, go to "Static files" section
- Add:
  - **URL**: `/media/`
  - **Directory**: `/home/yourusername/Convert/media`

### 9. Set Up Database
- Run migrations:
  ```bash
  python manage.py migrate
  ```

### 10. Update ALLOWED_HOSTS
- In `convert/settings.py`, change `ALLOWED_HOSTS = ['*']` to your actual domain:
  ```python
  ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
  ```

### 11. Reload the Web App
- Click the "Reload" button in the "Web" tab

## Important Notes:
- The project uses WeasyPrint for generating card images. This works on PythonAnywhere without special setup.
- In development (Windows), card generation may not work due to missing GTK+ libraries, but the app will show a friendly error message.
- On PythonAnywhere, card generation will work perfectly.
- SQLite is used as the database (suitable for small projects).
- DEBUG is set to False for production.
