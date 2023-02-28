FROM python:3.10


ENV PYTHONUNBUFFERRED=1

WORKDIR /code

COPY requirements.txt .



RUN pip install -r requirements.txt

ADD . /code/

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

