# Generated by Django 4.2.20 on 2025-03-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=50)),
                ('is_national_team', models.BooleanField(default=False)),
                ('last_performance', models.JSONField(blank=True, default=dict)),
                ('current_standings', models.JSONField(blank=True, default=dict)),
                ('silverware', models.IntegerField(default=0)),
                ('local_ranking', models.IntegerField(blank=True, null=True)),
                ('international_ranking', models.IntegerField(blank=True, null=True)),
                ('crest_url', models.URLField(blank=True, null=True)),
                ('market_value', models.FloatField(blank=True, null=True)),
                ('leagues', models.ManyToManyField(related_name='teams', to='competitions.competition')),
            ],
        ),
    ]
