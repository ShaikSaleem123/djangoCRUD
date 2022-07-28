FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /CRUD-project

COPY . /CRUD-project/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "43.205.146.198:8000"]
