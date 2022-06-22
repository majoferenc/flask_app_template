# Notes

## Create new Conda env

	conda create --name flask python=3.9

## Activate Conda env

	conda activate flask

## Install Flask for the first time
	
	pip install flask

## Create requirements.txt

	pip freeze > requirements.txt

## Run app via python

	python src/main.py

## Run with custom log level

	python src/main.py -logLevel=DEBUG

## Build container image

	podman build -t flask_project:0.1 .

## Run container image

	podman run -p 8080:8080 flask_project:0.1
