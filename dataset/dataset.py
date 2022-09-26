import json
import pandas as pd


class Data:
    def __init__(self, filepath: str):
        try:
            self.df = pd.read_csv(filepath)
        except Exception as e:
            raise e

    def insertDataset(self, model):
        """
        :model: model class instance
        """
        columns = [
            "total_vaccinations",
            "people_vaccinated",
            "people_fully_vaccinated",
            "daily_vaccinations_raw",
            "daily_vaccinations",
            "total_vaccinations_per_hundred",
            "people_vaccinated_per_hundred",
            "people_fully_vaccinated_per_hundred",
            "daily_vaccinations_per_million",
        ]

        if model.__name__ == "Country_vaccinations":
            for i in columns:
                index = self.df[~self.df[i].notnull()][i].index
                self.df.loc[index, i] = 0.0

        # dataFrame to list of dictionaries
        dic = list(json.loads(self.df.T.to_json()).values())

        insert = model.objects.add_dataset(dic)

        return insert

