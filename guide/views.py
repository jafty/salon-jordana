from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from .models import Post


CITY_PAGES = [
    {
        'slug': 'toulouse',
        'name': 'Toulouse',
        'intro': "Trouver une coiffure afro à Toulouse n'est pas toujours simple : disponibilités, savoir-faire sur cheveux crépus, et proximité comptent énormément.",
    },
    {
        'slug': 'blagnac',
        'name': 'Blagnac',
        'intro': "À Blagnac, la demande pour la coiffure afro progresse et plusieurs coiffeuses se déplacent aussi à domicile selon les besoins.",
    },
    {
        'slug': 'colomiers',
        'name': 'Colomiers',
        'intro': "Coiffure afro à Colomiers : tresses, vanilles, soins et coiffures protectrices accessibles sans aller jusqu'au centre de Toulouse.",
    },
    {
        'slug': 'tournefeuille',
        'name': 'Tournefeuille',
        'intro': "Pour une coiffure afro à Tournefeuille, l'objectif est de comparer les profils en fonction de vos cheveux, du style recherché et du budget.",
    },
]


class HomeView(ListView):
    template_name = 'guide/home.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_pages'] = CITY_PAGES
        return context


class ArticleDetailView(DetailView):
    template_name = 'guide/article_detail.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CityPageView(TemplateView):
    template_name = 'guide/city_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = next((item for item in CITY_PAGES if item['slug'] == self.kwargs['city_slug']), None)
        if city is None:
            raise Http404('City page not found')

        city_name = city['name']
        local_posts = Post.objects.filter(title__icontains=city_name)
        local_posts = local_posts | Post.objects.filter(excerpt__icontains=city_name)
        local_posts = local_posts | Post.objects.filter(content__icontains=city_name)
        local_posts = local_posts.distinct()[:12]

        posts = local_posts if local_posts else Post.objects.all()[:12]

        context.update(
            {
                'city': city,
                'posts': posts,
                'city_topic_links': [
                    {
                        'label': f"Idées coiffure afro à {city_name}",
                        'url': f"/categories/idees-coiffure-{city['slug']}/",
                    },
                    {
                        'label': f"Conseils entretien cheveux crépus à {city_name}",
                        'url': f"/categories/conseils-entretien-{city['slug']}/",
                    },
                    {
                        'label': f"Adresses beauté afro autour de {city_name}",
                        'url': f"/categories/adresses-beaute-{city['slug']}/",
                    },
                ],
            }
        )
        return context


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'})
