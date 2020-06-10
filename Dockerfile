FROM python:3.8-alpine AS intermediate
COPY requirements.txt /
RUN ["pip", "install", "-r", "/requirements.txt"]
FROM intermediate as catastrophe
COPY catastrophe/app.py /
ENTRYPOINT ["python", "/app.py"]
EXPOSE 5000/tcp