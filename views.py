from django.shortcuts import render, get_object_or_404

from blog.models import Article


def home(request):
    #запрос к БД на получение всех статей
    articles=Article.objects.all().order_by("-date")
    context={
        'articles':articles
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def contacts(request):
    return render(request, 'blog/contacts.html')

def show_article(request,article_id):
    #получение страницы, которая нужна или выдача 404 - необходимо импортировать данный метод
    article=get_object_or_404(Article,id=article_id)



    return render(request,'blog/article.html',{'article':article})

