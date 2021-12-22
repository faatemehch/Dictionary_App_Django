from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt


def index(request, *args, **kwargs):
    context = {
        'title': 'Dictionary App'
    }
    return render( request, 'dictionary/index.html', context )


@csrf_exempt
def get_definition(request, word):
    print( request.method )
    url = f'https://www.dictionary.com/browse/{word}'
    response = requests.get( url=url )
    # use BeautifulSoup to extract data from HTML
    soup = BeautifulSoup( response.content, 'html.parser' )
    # the definitions are in span tag so fine them
    spans = soup.find_all( 'span', {"class": "one-click-content"} )
    context = {
        'title': 'Dictionary App'
    }
    if len( spans ) != 0:
        context['word'] = word
        context['definition'] = spans[0].text
    else:
        context['word'] = word
        context['definition'] = 'Not found'
    return JsonResponse( context )
