FROM python:3
COPY . .

RUN pip install pandas

COPY ./ /app
WORKDIR /app

CMD python /app/file_parser.py