from django.urls import path
from .views import index

app_name = 'dictionary'
urlpatterns = [
    path( '', index, name='index_view' )
]
