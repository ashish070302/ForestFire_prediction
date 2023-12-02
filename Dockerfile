FROM continuumio/anaconda3:latest

WORKDIR /home

EXPOSE 5000

COPY . .

CMD ["python", "app.py"]

 