FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY req.txt /code/

RUN pip install -r req.txt
COPY ./conference_app /code/

RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["bash"]