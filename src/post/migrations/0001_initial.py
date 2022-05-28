# Generated by Django 4.0.4 on 2022-05-25 10:09

from django.db import migrations, models
import utils.snippets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('caption', models.TextField(verbose_name='Caption')),
                ('file', models.ImageField(blank=True, max_length=128, null=True, upload_to=utils.snippets.change_file_extension_post, verbose_name='Media')),
                ('reshare_count', models.PositiveIntegerField(default=0, verbose_name='Total Reshare')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='Total Comment')),
                ('like_count', models.PositiveIntegerField(default=0, verbose_name='Total Like')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]