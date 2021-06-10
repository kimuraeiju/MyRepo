# syntax=docker/dockerfile:1
FROM python:3.9-slim
#ENV http_proxy http://host.docker.internal:3128 -> Uses this to allow api calls from behind proxy
#ENV https_proxy http://host.docker.internal:3128 -> Uses this to allow api calls from behind proxy
WORKDIR C:\myGitHub\MyRepo\python\CreateWeatherHistogram
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "-m", "app"]