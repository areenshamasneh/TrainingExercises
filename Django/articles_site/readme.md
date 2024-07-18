# Articles Site

A Django project to manage articles categorized by year and month. Users can view articles, add new ones via the admin interface or shell, and access details for each article.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Entering New Articles](#entering-new-articles)
- [Database Configuration](#database-configuration)

## Prerequisites

- Python 3.11 or higher
- Django 5.0 or higher
- MySQL or MariaDB

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/areenshamasneh/TrainingExercises.git
   cd articles_site
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Project

To run the development server, use the following command:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/articles/` in your web browser to see the application in action.

## Entering New Articles

### Using the Admin Interface

1. Navigate to `http://127.0.0.1:8000/admin/`.
2. Log in with your superuser credentials.
3. Under the "Polls" section, select "Articles" to add new articles.

### Using the Shell

1. Open the shell:

   ```bash
   python manage.py shell
   ```

2. Use the following commands to create a new article:

   ```python
   from polls.models import Article
   new_article = Article(year=2024, month=7, slug='new-article', title='New Article Title')
   new_article.save()
   ```

## Database Configuration

Before running the project, update your database configuration in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "DBName",
        "USER": "root",
        "PASSWORD": "yourpass",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

**Important:** Change the `NAME`, `USER`, and `PASSWORD` to match your local MySQL/MariaDB setup.
