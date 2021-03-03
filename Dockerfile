FROM python:3.9-slim

COPY . /main
WORKDIR /main

# RUN pip install --upgrade pip

# RUN python -m unittest -v

CMD ["python", "app.py"]
