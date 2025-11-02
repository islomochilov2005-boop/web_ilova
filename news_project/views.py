from django.shortcuts import render
from .models import News, Category
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy


def all_news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/all_news.html', context)


def detail(request, news):
    new = News.objects.get(slug=news)
    context = {
        'new': new
    }
    return render(request, 'news/one.html', context)


def home_page_view(request):
    categories = Category.objects.all()
    news = News.objects.all()
    last_news = News.objects.order_by('-published_at')[:6]

    uzb_news_last = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="O'zbekiston").order_by("-published_at")[0]
    uzb_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="O'zbekiston").order_by("-published_at")[1:5]
    jahon_yangiliklari = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="jahon").order_by("-published_at")[0]
    jahon_yangiliklar = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="jahon").order_by("-published_at")[1:5]

    idtisodiyot_last_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="iqtisodiyot").order_by("-published_at")[0]
    iqtisod_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="iqtisodiyot").order_by("-published_at")[1:5]

    sport_last = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="sport").order_by("-published_at")[0]
    sport_last_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact="sport").order_by("-published_at")[1:4]

    news_video = News.objects.all().order_by('-published_at')

    for i in news_video:
        if str(i.video) != "":
            new_video = i
            break

    moliya_news = News.objects.select_related("category").filter(status=News.Status.Published,
                                                                 category__name__iexact="moliya").order_by(
        "-published_at")[1:5]
    images = News.objects.order_by('-published_at')[:6]

    context = {
        'categories': categories,
        'news': news,
        'last_news': last_news,
        'uzb_news_last': uzb_news_last,
        'uzb_news': uzb_news,
        'jahon_yangiliklari': jahon_yangiliklari,
        'jahon_yangiliklar': jahon_yangiliklar,
        'idtisodiyot_last_news': idtisodiyot_last_news,
        'iqtisod_news': iqtisod_news,
        'sport_last': sport_last,
        'sport_last_news': sport_last_news,
        'new_video': new_video,
        'moliya_news': moliya_news,
        'images': images
    }
    return render(request, 'news/index.html', context)


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("xabar adminga yuborildi ✔ <a href=''>Asosiy sahifa </a>")
    context = {
        'form': form
    }
    return render(request, 'news/contact.html', context)


def about_view(request):
    context = {}
    return render(request, 'news/about.html', context)


def for_base_html(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news
    }
    return render(request, 'news/base.html', context)


def category_news(request, ct_name):
    ct_news = News.objects.select_related("category").filter(status=News.Status.Published,category__name__iexact=ct_name.lower()).order_by(
        "-published_at")
    context = {
        'ct_news': ct_news,
        'ct_name': ct_name
    }
    return render(request, 'news/category_news.html', context)


class EditView(UpdateView):
    model = News
    template_name = 'crud/edit_news.html'
    fields = ['title','body','image','video','category','status']
    context_object_name = 'simple'


class RemoveView(DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url =reverse_lazy('home_page')
    context_object_name = 'salom'



class CreateNewsView(CreateView):
    model = News
    template_name = 'crud/create.html'
    fields = ['title','slug','body','image','video','category','status']
    context_object_name = 'alik'