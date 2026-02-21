from django.http import HttpResponse
from django.urls import path

from .views import ArticleDetailView, CityPageView, HealthCheckView, HomeView

app_name = 'guide'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('coiffure-afro/<slug:city_slug>/', CityPageView.as_view(), name='city_page'),
    path('healthz/', HealthCheckView.as_view(), name='healthz'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('categories/<slug:slug>/', lambda request, slug: HttpResponse(f'Category: {slug}'), name='category_detail'),
]
