from django.core.management.base import BaseCommand, CommandError
#Primero hacer migraciones
#Luego por medio del shell de django ejecutar las siguientes lineas de codigo

from applications.vaccinations_by_manufacturer.models import Vaccinations_by_manufacturer
from applications.country_vaccinations.models import Country_vaccinations
from dataset.dataset import Data


class Command(BaseCommand):
    help = "Filling the database with datasets"

    def handle(self, *args, **options):
        try:
            cl1 = Data('dataset/country_vaccinations_by_manufacturer.csv')
            cl2= Data('dataset/country_vaccinations.csv')

            cl1.insertDataset(Vaccinations_by_manufacturer)
            cl2.insertDataset(Country_vaccinations)

            self.stdout.write(
                self.style.SUCCESS('Datasets successfully inserted')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error: {e}')
            )