FROM python:3.7-slim
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
CMD ["python", "manage.py","run"]
