# Generated by Django 4.1.1 on 2023-01-24 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.CharField(choices=[('info', 'Info'), ('attention', 'Attention'), ('alarm', 'Alarm')], max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('info', 'Info'), ('attention', 'Attention'), ('alarm', 'Alarm')], max_length=255)),
                ('tags', models.ManyToManyField(related_name='events', to='main.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]