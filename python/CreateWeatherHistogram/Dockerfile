# syntax=docker/dockerfile:1
FROM python:3.9-slim
ENV input_arg ${inputfile_arg}
ENV output_arg ${outputfile_arg}
WORKDIR C:\myGitHub\MyRepo\python\CreateWeatherHistogram
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "-m", "CreateWeatherHistogram"]
CMD ["no_parameter_specified"]
