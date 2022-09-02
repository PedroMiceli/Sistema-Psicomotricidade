FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get unzip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./psicomotricidade/psicomotricidade/python manage.py runserver"]


EXPOSE 8080