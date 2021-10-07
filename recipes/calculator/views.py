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
    # можете добавить свои рецепты ;)
}


def food_view(request):
    context = {}
    recipe = {}
    count = 1
    if request.GET.get('servings'):
        count = int(request.GET.get('servings'))
    for el in DATA:
        if el in str(request):
            for key, value in DATA[el].items():
                recipe.update({key: value * count})
            context.update({'recipe': recipe})
            print(context)
    return render(request, 'calculator/index.html', context)

