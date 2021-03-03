FROM python:3.9-slim
COPY . /main
WORKDIR /main
CMD ["python", "app.py"]
