from django.db import models


class Country_vaccinations_manager(models.Manager):
    def __add_dataset(self, dataset):
        objs = [
            self.model(
                country=i["country"],
                iso_code=i["iso_code"],
                date=i["date"],
                total_vaccinations=i["total_vaccinations"],
                people_vaccinated=i["people_vaccinated"],
                people_fully_vaccinated=i["people_fully_vaccinated"],
                daily_vaccinations_raw=i["daily_vaccinations_raw"],
                daily_vaccinations=i["daily_vaccinations"],
                total_vaccinations_per_hundred=i["total_vaccinations_per_hundred"],
                people_vaccinated_per_hundred=i["people_vaccinated_per_hundred"],
                people_fully_vaccinated_per_hundred=i[
                    "people_fully_vaccinated_per_hundred"
                ],
                daily_vaccinations_per_million=i["daily_vaccinations_per_million"],
                vaccines=i["vaccines"],
                source_name=i["source_name"],
            )
            for i in dataset
        ]

        self.bulk_create(objs)


    def add_dataset(self, dataset):
        return self.__add_dataset(dataset)
