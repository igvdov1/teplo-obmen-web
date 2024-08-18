from django.shortcuts import render
from django.http import HttpResponse
from .models import TeploObmennik
from django.shortcuts import render, get_object_or_404
from .models import Year, ProductCard

def gallery(request):
    teploobmennik = TeploObmennik.objects.all()
    return render(request, 'gallery.html', {'teploobmennik': teploobmennik})

def main_window(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def service(request):
    return render(request, 'service.html')

def news(request): 
    return render(request, 'news.html')

def individual_projects(request): 
    return render(request, 'individual_projects.html')
# views.py

def about(request): 
    return render(request, 'about.html')

def show_partners(request):
    return render(request, 'partners.html')

def year_list(request):
    years = Year.objects.all()
    return render(request, 'year_list.html', {'years': years})

def product_cards_by_year(request, year_id):
    year = get_object_or_404(Year, id=year_id)
    product_cards = year.product_cards.all()
    return render(request, 'product_cards_by_year.html', {'year': year, 'product_cards': product_cards})
