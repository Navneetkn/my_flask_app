FROM python:alpine
WORKDIR /my_app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "my_app.py" ]