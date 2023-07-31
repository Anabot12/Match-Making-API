# Generated by Django 4.2.2 on 2023-07-05 18:01

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Swipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('liked_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.profile')),
                ('swiper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swipes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('swiper', 'liked_profile')},
            },
        ),
    ]