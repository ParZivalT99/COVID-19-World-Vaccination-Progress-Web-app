# pull the official base image
FROM python:3.10.12-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt


# copia de proyecto
COPY . /usr/src/app

EXPOSE 8000

# comando de ejecucion
CMD ["sh","entrypoint.sh"]