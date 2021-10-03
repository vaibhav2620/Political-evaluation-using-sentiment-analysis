import pandas as pd
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from sensitive_data import dataset,feature_set,no_of_items

# To calculate the basic probability of a word for a category
def calc_prob(word,category):

	if word not in feature_set or word not in dataset[category]:
		return 0

	return float(dataset[category][word])/no_of_items[category]


# Weighted probability of a word for a category
def weighted_prob(word,category):
	# basic probability of a word - calculated by calc_prob
	basic_prob=calc_prob(word,category)

	# total_no_of_appearances - in all the categories
	if word in feature_set:
		tot=sum(feature_set[word].values())
	else:
		tot=0
		
	# Weighted probability is given by the formula
	# (weight*assumedprobability + total_no_of_appearances*basic_probability)/(total_no_of_appearances+weight)
	# weight by default is taken as 1.0
	# assumed probability is 0.5 here
	weight_prob=((1.0*0.5)+(tot*basic_prob))/(1.0+tot)
	return weight_prob


# To get probability of the test data for the given category
def test_prob(test,category):
	# Split the test data
	split_data=re.split('[^a-zA-Z][\'][ ]',test)
	
	data=[]
	for i in split_data:
		if ' ' in i:
			i=i.split(' ')
			for j in i:
				if j not in data:
					data.append(j.lower())
		elif len(i) > 2 and i not in data:
			data.append(i.lower())

	p=1
	for i in data:
		p*=weighted_prob(i,category)
	return p


#dataclean today
def dataClean(string):    # clean data by removing html tags,numbers and stopwords.
    soup = BeautifulSoup(string,"lxml")
    html_gone = soup.get_text()
    numbers_gone = re.sub("[^a-zA-Z]"," ",html_gone)
    words = numbers_gone.lower().split()
    stops = set(stopwords.words("english"))
    stops_gone = [w for w in words if not w in stops]
    return " ".join(stops_gone)

# Naive Bayes implementation
def naive_bayes(test):
	#formula main
	results={}
	for i in dataset.keys():
		# Category Probability
		# Number of items in category/total number of items
		cat_prob=float(no_of_items[i])/sum(no_of_items.values())
        #print("cat", cat_prob)
		# p(test data | category)
		test_prob1=test_prob(test,i)

		results[i]=test_prob1*cat_prob
        

	return results

test_data = pd.read_csv('testData.tsv',header=0,sep='\t',quoting=3)
clean_test = []
test_num = test_data['review'].size
for i in range(0,test_num):
    clean_test.append(dataClean(test_data.review.iloc[i]))
if clean_test:
    print("Naive Bayes running..")
a1=[]

for i in clean_test:
    s=naive_bayes(i)
    if s["-1"]<s["1"]:
        a1.append(1)
    else:
        a1.append(0)
        

        
        
"""print( 'Enter the sentence : ')
text=input()
result=naive_bayes(text)
print(result)
if result['1'] < result['-1']:
	print ('Negative')
else:
	print ('Positive')"""