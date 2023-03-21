from django.shortcuts import render
from news.models import News


def index(request):
    context_dict = {}
    context_dict['list'] = News.objects.order_by('-date')

    return render(request, 'news/index.html', context=context_dict)
