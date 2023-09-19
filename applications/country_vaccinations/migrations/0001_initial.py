# Generated by Django 3.2.15 on 2023-09-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country_vaccinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('iso_code', models.CharField(max_length=20, verbose_name='Iso code')),
                ('date', models.CharField(max_length=15, verbose_name='Date')),
                ('total_vaccinations', models.FloatField(max_length=50, verbose_name='Total vaccinations')),
                ('people_vaccinated', models.FloatField(max_length=50, verbose_name='People vaccinated')),
                ('people_fully_vaccinated', models.FloatField(max_length=50, verbose_name='People fully vaccinated')),
                ('daily_vaccinations_raw', models.FloatField(max_length=50, verbose_name='Daily vaccinations raw')),
                ('daily_vaccinations', models.FloatField(max_length=50, verbose_name='Daily vaccinations')),
                ('total_vaccinations_per_hundred', models.FloatField(max_length=50, verbose_name='Total vaccinations per hundred')),
                ('people_vaccinated_per_hundred', models.FloatField(max_length=50, verbose_name='People vaccinated per hundred')),
                ('people_fully_vaccinated_per_hundred', models.FloatField(max_length=50, verbose_name='People fully vaccinated per hundred')),
                ('daily_vaccinations_per_million', models.FloatField(max_length=50, verbose_name='Daily vaccinations per million')),
                ('vaccines', models.CharField(max_length=150, verbose_name='vaccines')),
                ('source_name', models.CharField(max_length=80, verbose_name='source_name')),
            ],
            options={
                'verbose_name': 'Country_vaccination',
                'verbose_name_plural': 'Country_vaccinations',
            },
        ),
    ]
