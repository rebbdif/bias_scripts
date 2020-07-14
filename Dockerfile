FROM python:3
WORKDIR /scripts

COPY . .
CMD ["pip install pandas"]