
from unicodedata import name
from . import views
from django.urls import path


urlpatterns =[
    path('', views.index, name='index'),
    path('tambahcashflow', views.tambahCashflow, name='tambahcashflow'),
    path('hapuscashflow/<str:pk>', views.hapusCashFlow, name='hapuscashflow'),
]