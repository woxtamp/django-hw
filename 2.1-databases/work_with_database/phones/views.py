from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    sort = request.GET.get('sort')
    if sort == None or sort == 'name':
        all_phones = Phone.objects.all().order_by('name')
        context['phones'] = all_phones
        return render(request, template, context)
    elif sort == 'min_price':
        all_phones = Phone.objects.all().order_by('price')
        context['phones'] = all_phones
        return render(request, template, context)
    elif sort == 'max_price':
        all_phones = Phone.objects.all().order_by('-price')
        context['phones'] = all_phones
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone' : phone}
    return render(request, template, context)