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

def recipes(request, recipe):
    recipe = DATA.get(recipe)
    servings = int(request.GET.get('servings', 0))
    if recipe and servings > 0:
        recipe = dict(map(lambda i: (i[0], i[1]*servings), recipe.items()))

    return render(request, 'calculator/index.html', {'recipe': recipe})
