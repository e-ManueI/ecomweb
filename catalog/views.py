from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product
from django.views.generic import ListView, TemplateView
from django.template import RequestContext
# Create your views here.
class IndexView(TemplateView):
    http_method_names = ["get"]
    page_title = 'Catalog - Buy your dream product'
    template_name = "index.html"

class CategoryView(ListView):
    model = Category
    page_title = Category.name
    
    