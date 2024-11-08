Spy Cat Agency (SCA) Management API

A RESTful API built with Django and Django REST Framework for managing spy cats, missions, and targets for the Spy Cat Agency (SCA). This API enables SCA to handle the full lifecycle of spy cats, assign them to missions, and manage targets efficiently.

Features:

    Spy Cats Management:
        Add, update, view, and delete spy cats
        Retrieve a list of all spy cats or a single cat
        Update spy cat salary
        Validate cat breed using TheCatAPI

    Mission and Target Management:
        Create new missions with targets in a single request
        Assign a mission to a specific spy cat
        Update target notes and mark targets as complete
        Mark a mission as complete once all associated targets are complete
        Prevent note updates on completed targets or missions
        Delete a mission only if it has not been assigned to a cat

Requirements:

    Python 3.8+
    Django 3.2+
    Django REST Framework
    PostgreSQL (or any other SQL-like database)
    django-filter (for filtering capabilities)
    requests (for external breed validation with TheCatAPI)
    TheCatAPI key for breed validation

Installation:
1. Clone the repository:
```bash 
git clone https://github.com/yourusername/spy-cat-agency-api.git
cd spy-cat-agency-api
```
2. Create a virtual environment:
```bash python3 -m venv env
source env/bin/activate
```
3. Install dependencies:
```bash 
pip install -r requirements.txt
```
4. Set up environment variables:
```bash 
SECRET_KEY=<your_django_secret_key>
DEBUG=True
DATABASE_URL=postgres://<user>:<password>@localhost:5432/spy_cat_db
THE_CAT_BREED_API_KEY=<your_thecatapi_key>
```
5. Set up the database:
```bash 
python manage.py migrate
```
6. Create a superuser (optional but recommended for admin access):
```bash 
python manage.py createsuperuser
```
7. Start the development server:
```bash 
python manage.py runserver
```
