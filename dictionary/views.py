from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request, *args, **kwargs):
    context = {
        'title': 'Dictionary App'
    }
    if request.method == 'GET':
        return render( request, 'dictionary/index.html', context )
    elif request.method == 'POST':
        print( request.method )
        word = request.POST.get( 'word' )
        url = f'https://www.dictionary.com/browse/{word}'
        response = requests.get( url=url )
        # use BeautifulSoup to extract data from HTML
        soup = BeautifulSoup( response.content, 'html.parser' )
        # the definitions are in span tag so fine them
        spans = soup.find_all( 'span', {"class": "one-click-content"} )
        print( spans[0].text )
        context['word'] = word
        context['definition'] = spans[0].text
        # return render( request, 'dictionary/index.html', context )
        return JsonResponse( context )
