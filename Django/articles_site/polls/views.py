from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Article


def home(request):
    return render(request, "home.html")


def all_articles(request):
    try:
        query = request.GET.get("search", "")
        articles = Article.objects.all()

        if query:
            articles = articles.filter(
                Q(title__icontains=query)
                | Q(slug__icontains=query)
                | Q(content__icontains=query)
            )

        return render(
            request, "all_articles.html", {
                "articles": articles, "search": query}
        )

    except Exception as e:
        return render(request, "error.html", {"error": str(e)})


def articles_by_year(request, year):
    try:
        articles = Article.objects.filter(year=year)

        if not articles.exists():
            raise Http404("No articles found for this year")

        return render(request, "articles.html", {"year": year, "articles": articles})

    except Exception as e:
        return render(request, "error.html", {"error": str(e)})


def articles_by_month(request, year, month):
    try:
        articles = Article.objects.filter(year=year, month=month)

        if not articles.exists():
            raise Http404("No articles found for this year and month")

        return render(
            request, "articles.html", {
                "year": year, "month": month, "articles": articles}
        )

    except Exception as e:
        return render(request, "error.html", {"error": str(e)})


def article_detail(request, year, month, slug):
    try:
        article = get_object_or_404(Article, year=year, month=month, slug=slug)
        return render(request, "article_detail.html", {"article": article})
    except Http404:
        return render(request, "error.html", status=404)
