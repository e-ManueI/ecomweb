from multiprocessing import context
from pipes import Template
from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product
from django.views.generic import ListView, TemplateView
from django.template import RequestContext
# Create your views here.
class IndexView(TemplateView):
    http_method_names = ["get"]
    page_title = 'Catalog - Buy your dream product'
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-updated_at')[0:20]
        return context
    
class CategoryView(TemplateView):
    model = Category
    page_title = Category.name
    template_name = "categories.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('-updated_at')[0:20]
        return context
    
    