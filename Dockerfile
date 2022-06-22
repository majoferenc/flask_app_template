FROM python:3.9-slim-bullseye

LABEL description="This is an example flask app" \
      io.k8s.description="This is an example flask app" \
      io.openshift.tags="flask_project" \
      io.openshift.exposeservices="8080" \
      io.openshift.min-memory="100Mi" \
      io.openshift.min-cpu="300m" \
      version="0.1" \
      creationDate="22.6.2022"

WORKDIR /flask_project

COPY src .

RUN pip install -r requirements.txt

USER 1001

EXPOSE 8080

CMD python3 main.py
