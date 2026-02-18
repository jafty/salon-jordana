from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('guide:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.name)
        slug = base_slug
        counter = 2
        while Category.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        return slug


class Post(models.Model):
    class LayoutType(models.TextChoices):
        STANDARD = 'standard', 'Standard'
        LARGE = 'large', 'Large (span 2)'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    excerpt = models.CharField(max_length=320)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    layout_type = models.CharField(
        max_length=20,
        choices=LayoutType.choices,
        default=LayoutType.STANDARD,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('guide:article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 2
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        return slug
