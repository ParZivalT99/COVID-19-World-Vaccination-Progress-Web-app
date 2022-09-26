# COVID-19 World Vaccination Progress Web app
Fuente de los [dataset](https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress?resource=download&select=country_vaccinations_by_manufacturer.csv)

## Llenar la base de datos
  ```
  #Primero hacer migraciones
  #Luego por medio del shell de django ejecutar las siguientes lineas de codigo
	>>>from applications.vaccinations_by_manufacturer.models import Vaccinations_by_manufacturer
  >>>from applications.country_vaccinations.models import Country_vaccinations
  >>>from dataset.dataset import Data
  
  >>>cl1 = Data('dataset/country_vaccinations_by_manufacturer.csv')
  >>>cl2= Data('dataset/country_vaccinations.csv')
  >>>cl1.insertDataset(Vaccinations_by_manufacturer)
  >>>cl2.insertDataset(Country_vaccinations)
	```
  
  
  
