# Hacker Rank temperature histogram

## Instructions:
* Build the docker image:\
    
    Build the docker image behind a proxy:\
    `docker build --no-cache --network=host --build-arg HTTP_PROXY=http://host.docker.internal:3128 --build-arg HTTPS_PROXY=http://host.docker.internal:3128 -t <image_name> .`
    
    Build the docker image without a proxy:\
    `docker build --no-cache -t <image_name> .`

* Run the docker image:\
`docker run --mount type=bind,source=c:\dir\of\the\code,target=/app <image_name> --inputfile forecast_data.csv --outputfile out_put.png --bucketcount 5`

* To view the output:\
Once the docker has finished running the output files should be saved to the directory of where the docker files are.

### Disclaimer
I have tried to complet this task as best to my abilities. There are several differences to what was requested in the test:
- The results fo the histogram is most likely incorrect, but just want to emphasis that I'm not from a data science background and my skillset and expertise is in the infrastructure and networking aspect.
- I'm using a different input file and different API call compared to the one provided as I don't think I will be able to decipher the log file in time and provide a meaningful output, I've decided to demonstrate I have the understanding of the underlaying ask:
    1. extract data from an input file and manipulate it to provide an output
    2. understand how to perform API calls and to able to process the responses and give a meaningful output
    3. the ability to create a docker container that takes an input from the host machine
    4. the ability for the docker container to output to the host machine for later usage