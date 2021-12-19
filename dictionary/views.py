from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request, *args, **kwargs):
    print( request.method )
    context = {
        'title': 'Dictionary App'
    }
    if request.method == 'GET':
        return render( request, 'dictionary/index.html', context )
    if request.GET.get( 'word' ) is not None:
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
        print( context )
        return JsonResponse( context )


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
