FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8000
CMD [ "python", "psicomotricidade/manage.py", "runserver", "0.0.0.0:8000" ]

