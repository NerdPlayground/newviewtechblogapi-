# Generated by Django 4.0.2 on 2022-02-12 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=255)),
                ('comment_created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_updated_at', models.DateTimeField(auto_now=True)),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('comment_under', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blog')),
            ],
        ),
    ]
