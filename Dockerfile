FROM python:3.9
ENV URL="http://192.168.0.105:8090/"
ENV BROWSER="chrome"
ENV LOG_LEVEL="DEBUG"
ENV EXECUTOR="192.168.0.105"
ENV MAXIMIZED="maximized"

WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD pytest --url=$URL --browser=$BROWSER --log_level=$LOG_LEVEL --executor=$EXECUTOR --maximized