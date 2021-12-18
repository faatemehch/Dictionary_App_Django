from django.shortcuts import render
import requests


def index(request, *args, **kwargs):
    context = {
        'title': 'Dictionary App'
    }
    if request.method == 'GET':
        return render( request, 'dictionary/index.html', context )
    elif request.method == 'POST':
        word = request.POST.get('word')
        url = f'https://www.dictionary.com/browse/{word}'
        response = requests.get( url=url )
        return render( request, 'dictionary/index.html', context )
