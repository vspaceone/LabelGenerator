FROM python:3-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python3-opencv

COPY . .
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 5007

CMD [ "python", "src/main/Server.py" ]
