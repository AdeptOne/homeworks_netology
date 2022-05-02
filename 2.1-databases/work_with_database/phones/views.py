from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_by = request.GET.get('sort')

    phones = Phone.objects.all()

    if sorted_by is not None:
        if sorted_by == 'max_price':
            phones = Phone.objects.order_by('-price')
        elif sorted_by == 'min_price':
            phones = Phone.objects.order_by('price')
        else:
            phones = Phone.objects.order_by('name')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
