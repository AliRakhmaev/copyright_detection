FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
COPY . /code/