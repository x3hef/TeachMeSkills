# Generated manually for homework project

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('meeting_time', models.DateTimeField()),
                ('place', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(blank=True, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
