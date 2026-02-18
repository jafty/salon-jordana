from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=220, unique=True)),
                ('excerpt', models.CharField(max_length=320)),
                ('content', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('is_featured', models.BooleanField(default=False)),
                ('layout_type', models.CharField(choices=[('standard', 'Standard'), ('large', 'Large (span 2)')], default='standard', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='guide.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
