from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    match request.GET.get('sort', 'default'):
        case 'name':
            phones = Phone.objects.order_by('name')
        case 'min_price':
            phones = Phone.objects.order_by('price')
        case 'max_price':
            phones = Phone.objects.order_by('-price')
        case _:
            phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug__exact=slug)
    }
    return render(request, template, context)
