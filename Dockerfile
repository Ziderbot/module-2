FROM python:3.12

WORKDIR /Isakov

COPY . /Isakov

CMD ["python", "variant8.py"]