FROM python:3.9

WORKDIR /flask_project

COPY src .

RUN pip install -r requirements.txt

USER 1001

EXPOSE 8080

CMD python3 main.py
