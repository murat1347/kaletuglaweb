FROM python:3.8-alpine

RUN pip install django

RUN pip install django-cleanup

RUN pip install django-crispy-forms

RUN pip install django-ckeditor

ADD src /src

CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8080"]

