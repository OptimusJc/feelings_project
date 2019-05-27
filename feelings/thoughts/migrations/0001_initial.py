# Generated by Django 2.0 on 2019-05-27 14:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(default=datetime.datetime(2019, 5, 27, 14, 38, 47, 420785, tzinfo=utc), editable=False)),
                ('condition', models.IntegerField(choices=[(2, 'Passionate'), (7, 'Pessimistic'), (10, 'Jealous'), (4, 'Optimistic'), (6, 'Bored'), (5, 'Content'), (8, 'Doubt'), (9, 'Worried'), (3, 'Frustrated'), (1, 'Joy'), (11, 'Fear'), (13, 'Tired'), (12, 'Hungry')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
