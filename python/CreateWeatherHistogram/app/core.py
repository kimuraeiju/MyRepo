import csv
import pandas as pd
import numpy as np
import requests as rq
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

def main(inputfile, outputfile, bucketcount):
    
    dir = "/app/"+outputfile
    api_dir = "/app/hist_api.png"

    temp_data = pd.read_csv(inputfile, usecols=[17])

    temp_data['Temperature'].hist(bins=bucketcount)
    plt.savefig(dir, bbox_inches='tight', dpi=100)

    
    api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?aggregateHours=24&combinationMethod=aggregate&startDateTime=2021-05-01T00%3A00%3A00&endDateTime=2021-06-10T00%3A00%3A00&maxStations=-1&maxDistance=-1&contentType=csv&unitGroup=metric&locationMode=single&key=5P2L73TBYGGGZKSUTCBFVFKEA&dataElements=default&locations=sydney"
    r = rq.get(api_url, verify=False)
    decoded_content = r.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',', quotechar='"')
    
    with open('api_csv.csv', mode='w') as api_csv:
        api_csv_writer = csv.writer(api_csv, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        api_csv_writer.writerows(cr)

    temp_data_api = pd.read_csv("api_csv.csv", usecols=[4])
    temp_data_api['Temperature'].hist(bins=bucketcount)
    plt.savefig(api_dir, bbox_inches='tight', dpi=100)
