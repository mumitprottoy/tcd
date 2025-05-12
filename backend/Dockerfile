FROM python:3.11-slim

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5959

ENV DJANGO_SETTINGS_MODULE=testcraft.settings

CMD ["tail", "-f", "/dev/null"]