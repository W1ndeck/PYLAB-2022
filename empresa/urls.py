from django.urls import path, include
from . import views
urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name='nova_empresa') #quando alguem acessar esse caminho retorne essa função
]
