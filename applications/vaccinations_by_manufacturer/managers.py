from django.db import models


class Vaccinations_by_manufacturer_manager(models.Manager):
    def __add_dataset(self, dataset):
        objs = [
            self.model(
                location=i["location"],
                date=i["date"],
                vaccine=i["vaccine"],
                total_vaccinations=i["total_vaccinations"],
            )
            for i in dataset
        ]
        # raw_data.save(using=self.db)
        self.bulk_create(objs)

    # metodo para crear registro de un historial
    def add_dataset(self, dataset):
        return self.__add_dataset(dataset)
