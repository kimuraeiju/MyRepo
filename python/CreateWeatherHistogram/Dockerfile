# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR C:\myGitHub\MyRepo\python\CreateWeatherHistogram
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .
CMD ["temp_histogram.py"]
ENTRYPOINT ["python3"]
