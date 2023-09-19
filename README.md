# COVID-19 World Vaccination Progress Web app

Aplicación web y API REST con autenticacion sobre el progreso de la vacunación en el mundo contra el COVID-19

> Fuente de los [dataset](https://www.kaggle.com/datasets/gpreda/covid-world-vaccination-progress?resource=download&select=country_vaccinations_by_manufacturer.csv)

## Ejecutar localmente
1. Crear el archivo .env, el cual debe de tener las siguientes variables:
```
  SECRET_KEY = ''
  DB_NAME = ''
  DB_USER = ''
  DB_PASS = ''
  DB_HOST = 'db'
  DB_PORT = '5432'
  DB_SCHEMA = 'public'
```
2. Ejecutar [docker-compose.yaml](https://github.com/ParZivalT99/COVID-19-World-Vaccination-Progress-Web-app/blob/main/docker-compose.yaml)
```
  # Ejecutar docker-compose
  docker-compose up -d --build
```
3. Crear superuser

## Referencia de API
- ### Vacunacion por pais

  #### Obtener todos los elementos.

  ```http
    GET /api/v1/vaccinations-by-country/
  ```

  #### Obtener elementos por id.

  ```http
    GET /api/v1/vaccinations-by-country/<pk>/
  ```

  | Parameter | Type     | Description                       |
  | :-------- | :------- | :-------------------------------- |
  | `id`      | `int` |   **Requiere**. Id de la vacunacion  |

  #### Obtener elementos por codigo iso.

  ```http
    GET /api/v1/vaccinations-by-country/iso-code/<iso_code_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `iso_code`| `str` |   **Requiere**. codigo iso del algun pais|


  #### Obtener elementos por fecha.

  ```http
    GET /api/v1/vaccinations-by-country/date/<date_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `date`    | `str`    | **Requiere**. fecha con formato Y-M-D|

  #### Obtener elementos por codigo iso y fecha.

  ```http
    GET /api/v1/vaccinations-by-country/iso-code-date/<iso_code_pk>/<date_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `iso_code`| `str`    | **Requiere**. codigo iso del algun pais|
  | `date`    | `str`    | **Requiere**. fecha con formato Y-M-D|

- ### Vacunacion por fabricante

  #### Obtener todos los elementos.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/
  ```

  #### Obtener elementos por id.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/<pk>/
  ```

  | Parameter | Type     | Description                       |
  | :-------- | :------- | :-------------------------------- |
  | `id`      | `int` |   **Requiere**. Id del elemento  |

  #### Obtener elementos por pais.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/location/<location_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `location`| `str` |   **Requiere**. Nombre de un pais|


  #### Obtener elementos por fecha.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/date/<date_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `date`    | `str`    | **Requiere**. fecha con formato Y-M-D|

  #### Obtener elementos por fabricante.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/vaccine/<vaccine_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `vaccine` | `str`    | **Requiere**. Nombre de un fabricante|


  #### Obtener elementos por pais fecah y fabricante.

  ```http
    GET /api/v1/vaccinations-by-manufacturer/location-date-vaccine/<location_pk>/<date_pk>/<vaccine_pk>/
  ```

  | Parameter | Type     | Description                        |
  | :-------- | :------- | :--------------------------------  |
  | `location`| `str` |   **Requiere**. Nombre de un pais|
  | `date`    | `str`    | **Requiere**. fecha con formato Y-M-D|
  | `vaccine` | `str`    | **Requiere**. Nombre de un fabricante|


## Resumen técnico
- Python
- Django
- Django REST Framework
- Postgres
- Docker
- HTML
- CSS
- Bootstrap

## Autor
- [Marcos Montes](https://github.com/ParZivalT99)

  
  
