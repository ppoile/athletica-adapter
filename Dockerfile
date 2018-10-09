FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD uwsgi --http :8000 --module athletica.wsgi
