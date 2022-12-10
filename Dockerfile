FROM python:alpine

WORKDIR /my_app

COPY . .

RUN pip install -r requirement.txt

EXPOSE 5000

CMD [ "python3", "my_app.py" ]