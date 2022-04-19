from django.urls import URLPattern
from django.urls import path
from .views import IndexView, CategoryView

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>', CategoryView.as_view(), name='categories')
]