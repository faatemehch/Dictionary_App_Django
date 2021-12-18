from django.shortcuts import render


def index(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'title': 'Dictionary App'
        }
        return render( request, 'dictionary/index.html', context )
