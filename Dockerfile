FROM python:3.9-slim

WORKDIR /

COPY . .

CMD [ "python", "driver.py" ]