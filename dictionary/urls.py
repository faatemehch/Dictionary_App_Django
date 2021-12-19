from django.urls import path
from .views import index, get_definition

app_name = 'dictionary'
urlpatterns = [
    path( '', index, name='index_view' ),
    path( 'definition/<str:word>/', get_definition, name='definition' ),
]
