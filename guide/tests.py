from django.test import TestCase
from django.urls import reverse

from .models import Category, Post


class CategoryModelTests(TestCase):
    def test_category_slug_is_generated_on_create(self):
        category = Category.objects.create(name='Salon de Coiffure')
        self.assertEqual(category.slug, 'salon-de-coiffure')

    def test_category_absolute_url(self):
        category = Category.objects.create(name='Conseils')
        self.assertEqual(category.get_absolute_url(), reverse('guide:category_detail', kwargs={'slug': category.slug}))


class PostModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Boutiques')

    def test_post_slug_is_generated_on_create(self):
        post = Post.objects.create(
            title='Ebène & Boucles : Le spa du cheveu crépu',
            category=self.category,
            excerpt='Un superbe salon à Carmes.',
            content='Contenu de test',
        )
        self.assertEqual(post.slug, 'ebene-boucles-le-spa-du-cheveu-crepu')

    def test_post_absolute_url(self):
        post = Post.objects.create(
            title='Afro Shop 31',
            category=self.category,
            excerpt='Adresse incontournable',
            content='Détails de la boutique',
        )
        self.assertEqual(post.get_absolute_url(), reverse('guide:article_detail', kwargs={'slug': post.slug}))

    def test_layout_type_defaults_to_standard(self):
        post = Post.objects.create(
            title='Le Bar à Tresses',
            category=self.category,
            excerpt='Spécialiste tressage',
            content='Texte',
        )
        self.assertEqual(post.layout_type, Post.LayoutType.STANDARD)


class UrlResolutionTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Salons')
        self.post = Post.objects.create(
            title='Fade Masters Toulouse',
            category=self.category,
            excerpt='Les meilleurs dégradés',
            content='Contenu article',
        )

    def test_home_url_resolves(self):
        response = self.client.get(reverse('guide:home'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves(self):
        response = self.client.get(self.post.get_absolute_url(), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_healthz_url_resolves(self):
        response = self.client.get(reverse('guide:healthz'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok'})

    def test_city_page_url_resolves(self):
        response = self.client.get(reverse('guide:city_page', kwargs={'city_slug': 'toulouse'}), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blog Coiffure Afro à Toulouse')


    def test_city_page_uses_blog_fallback_without_provider_wording(self):
        other_post = Post.objects.create(
            title='Routine cheveux crépus hiver',
            category=self.category,
            excerpt='Conseils pratiques',
            content='Contenu de test',
        )

        response = self.client.get(reverse('guide:city_page', kwargs={'city_slug': 'blagnac'}), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, other_post.title)
        self.assertNotContains(response, 'prestataire')


    def test_city_page_404_for_unknown_city(self):
        response = self.client.get(reverse('guide:city_page', kwargs={'city_slug': 'unknown'}), follow=True)
        self.assertEqual(response.status_code, 404)
