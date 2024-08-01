from django.core.management.base import BaseCommand
from polls.models import Article


class Command(BaseCommand):
    help = "Add sample articles to the database"

    def handle(self, *args, **kwargs):
        articles = [
            {
                "year": 2023,
                "month": 4,
                "slug": "introduction-to-python",
                "title": "Introduction to Python",
                "content": "A beginner-friendly guide to learning Python programming language.",
            },
            {
                "year": 2023,
                "month": 8,
                "slug": "data-analysis-with-pandas",
                "title": "Data Analysis with Pandas",
                "content": "Using Pandas library to manipulate and analyze data in Python.",
            },
            {
                "year": 2023,
                "month": 9,
                "slug": "machine-learning-basics",
                "title": "Machine Learning Basics",
                "content": "An overview of machine learning algorithms and applications.",
            },
            {
                "year": 2023,
                "month": 12,
                "slug": "web-development-with-django",
                "title": "Web Development with Django",
                "content": "Building web applications using Django framework.",
            },
            {
                "year": 2023,
                "month": 11,
                "slug": "deploying-web-applications",
                "title": "Deploying Web Applications",
                "content": "Strategies and best practices for deploying web applications.",
            },
        ]

        for article_data in articles:
            article, created = Article.objects.get_or_create(**article_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Article '{article.title}' created")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Article '{article.title}' already exists")
                )
