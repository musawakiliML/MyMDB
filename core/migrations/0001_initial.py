# Generated by Django 4.2.1 on 2023-05-22 14:06
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('plot', models.TextField()),
                ('year', models.PositiveIntegerField()),
                ('rating', models.IntegerField(choices=[(0, 'NR - Not Rated'), (1, 'G - General Audiences'), (2, 'PG - Parental Guidance'), (3, 'R - Restricted')], default=0)),
                ('runtime', models.PositiveIntegerField()),
                ('website', models.URLField(blank=True)),
            ],
        ),
    ]
