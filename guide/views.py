from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Post


class HomeView(ListView):
    template_name = 'guide/home.html'
    model = Post
    context_object_name = 'posts'


class ArticleDetailView(DetailView):
    template_name = 'guide/article_detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'})
