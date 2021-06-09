#import numpy as np
#from collections import Counter
#from numpy.core.fromnumeric import size
#from numpy.lib.polynomial import _binary_op_dispatcher

def main(inputfile, outputfile, bucketcount):
    
    dir = "/app/"+outputfile

    print("Output from CreateWeatherHistogram app")
    infile = open(inputfile,"r")
    if infile.mode == "r":
        infile_content = infile.read()
    print(infile_content)
    infile.close()

    outputfile_obj = open(dir, "w+")
    outputfile_obj.write("processed contents from inputfile with a bucketcount of %s" % bucketcount)
    outputfile_obj.close()

    outfile = open(dir, "r")
    if outfile.mode == "r":
        outfile_content = outfile.read()
        print(outfile_content)
    outfile.close()

    #https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/sydney?unitGroup=metric&key=5P2L73TBYGGGZKSUTCBFVFKEA
    
    #np.random.seed(444)
    #np.set_printoptions(precision=3)

    #d = np.random.laplace(loc=15, scale=3, size=500)
    #d[:5]
    #hist, bin_edges = np.histogram(d)

    #a = (1, 2, 4, 40, 12, 15, 10, 22, 9, 5, 30, 21)
    #def count_elements(seq) -> dict:
    #    hist = {}
    #    for i in seq:
    #        hist[i] = hist.get(i, 0) + 1
    #    return hist

    #bcounts = np.bincount(a)
    #hist, _ =np.histogram(a, range=(0, a.max()), bins=a.max() +1)
    #dict(zip(np.unique(a), bcounts[bcounts.nonzero()]))

    #counted = count_elements(a)
    #recounted = Counter(a)
