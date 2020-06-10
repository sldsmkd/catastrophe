pip freeze > requirements.txt
docker build . -t catastrophe:latest
docker run -p 5000:5000 catastrophe:latest
