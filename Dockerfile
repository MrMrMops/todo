FROM python:3
WORKDIR /usr/src/app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


COPY . ./
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt

