from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "article_form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    article_comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        "article": article,
        "comment_form": comment_form,
        "article_comments": article_comments,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect("articles:detail", article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            "article_form": form,
        }
        return render(request, "articles/update.html", context)
    else:
        return HttpResponseForbidden()  # 이거 잘 작동되는 건지 모르겠네요.


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            article.delete()
            return redirect("articles:index")
    else:
        return HttpResponseForbidden()  # 이거 잘 작동되는 건지 모르겠네요.


def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.article = article
                comment.save()
                messages.success(request, "댓글 달기 성공.")
                return redirect("articles:detail", article.pk)
        messages.warning(request, "잘못된 형식의 댓글.")
        return redirect("articles:detail", article.pk)
    else:
        return HttpResponseForbidden()  # 이거 잘 작동되는 건지 모르겠네요.
