# Generated by Django 3.2.4 on 2021-11-22 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=70)),
                ('contenuto', models.TextField()),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('argomento', models.CharField(choices=[('CRYPTO', 'Crypto'), ('ADESSO_NEL_MONDO', 'Adesso nel mondo'), ('ECONOMIA', 'Economia'), ('TECNOLOGIA', 'Tecnologia')], max_length=70)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
