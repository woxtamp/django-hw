from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home(request):
    pages = {
        'Рецепт омлета': '/omlet',
        'Рецепт пасты': '/pasta',
        'Рецепт бутерброда': '/buter',
    }
    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)


def recipes(request, recipe):
    servings = int(request.GET.get('servings', 1))

    context = dict()

    if recipe in DATA:
        context['recipes'] = DATA[recipe]
        for key, value in context['recipes'].items():
            context['recipes'][key] = value * servings

    return render(request, 'calculator/index.html', context)
