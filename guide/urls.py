from django.http import HttpResponse
from django.urls import path

from .views import ArticleDetailView, HealthCheckView, HomeView

app_name = 'guide'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('healthz/', HealthCheckView.as_view(), name='healthz'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('categories/<slug:slug>/', lambda request, slug: HttpResponse(f'Category: {slug}'), name='category_detail'),
]
