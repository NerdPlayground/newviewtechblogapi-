# Generated by Django 4.0.2 on 2022-02-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=255)),
                ('comment_created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
