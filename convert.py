import numpy as np 
import pandas as pd
from naive_main import a1



from bs4 import BeautifulSoup  #remove html tags
from nltk.corpus import stopwords  #words having high frequency like "the"
import re 
def dataClean(string):    # clean data by removing html tags,numbers and stopwords.
    soup = BeautifulSoup(string,"lxml")
    html_gone = soup.get_text()
    numbers_gone = re.sub("[^a-zA-Z]"," ",html_gone)
    words = numbers_gone.lower().split()
    stops = set(stopwords.words("english"))
    stops_gone = [w for w in words if not w in stops]
    return " ".join(stops_gone)


test_data  = pd.read_csv("labeledTrainData.tsv",sep='\t',header=0,quoting=3)
clean_test = []
test_num = test_data['review'].size
for i in range(0,test_num):
    clean_test.append(dataClean(test_data.review.iloc[i]))

print(clean_test)
for i in range(len(clean_test)):
    if test_data["sentiment"][i]:
        clean_test[i]=clean_test[i]+"+"+str(test_data["sentiment"][i])
    else:
        clean_test[i]=clean_test[i]+"+-1"
print(clean_test)

output = pd.DataFrame({char for char in clean_test[::]})
output.to_csv('naivetraining.csv',index=False,quoting=3)
