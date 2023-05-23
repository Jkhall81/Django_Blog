from django.shortcuts import render

posts = [
    {
        'author': 'JasonH',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 22, 2023'
    },
{
        'author': 'JasonKH',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 22, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


