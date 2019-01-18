


import numpy as np
import pandas as pd
import argparse



ap = argparse.ArgumentParser()
ap.add_argument("--file", required=True,help="Name of file")
args = vars(ap.parse_args())

df = pd.read_csv(args["file"])




import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)



dd = df[["Question 1","Question 2"]]

dd = dd.astype(str)




g = list()





for index,rows in dd.iterrows():
    text1  = rows["Question 1"]
    text2  = rows["Question 2"]
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)
    g.append(cosine)
    
    
    np.savetxt('output.txt', np.array(g), fmt='%.4f')
    

