from collections import Counter
import numpy as np

temp_input = (1,2,4,40,12,15,10,22,9,-10,-15,21)
def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_elements(temp_input)
recounted = Counter(temp_input)

print (recounted)
print (counted)