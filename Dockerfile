FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /CRUD-project

RUN pip install --upgrade pip

COPY requirements.txt /CRUD-project/

RUN pip install -r requirements.txt

COPY . /CRUD-project/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]