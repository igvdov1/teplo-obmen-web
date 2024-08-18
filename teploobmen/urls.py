from django.urls import path 
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name = 'gallery'),
    path('', views.main_window, name = 'teploobmen'),
    path('contact/', views.contact, name = 'contact'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('service/', views.service, name = 'service'),
    path('news/', views.news, name = 'news'),
    path('about/', views.about, name = 'about'),
    path('partners/', views.show_partners, name = 'partners'),
    path('year_list', views.year_list, name='year_list'),
    path('<int:year_id>/', views.product_cards_by_year, name='product_cards_by_year'),
    path('individual_projects/', views.individual_projects, name='individual_projects')
]
