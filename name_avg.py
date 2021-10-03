import pandas as pd
test_data = pd.read_csv('answer.csv')
#print(test_data["random"][9])
a=[]
for i in range(len(test_data)):
    a.append((test_data["random"][i]+test_data["naive"][i])/2)    
#print(a)

output = pd.DataFrame({'random':test_data["random"],"naive":test_data["naive"],"name":test_data["name"],"avg":a})
output.to_csv('answer.csv',index=False,quoting=3)

pos_na = 0
pos_ra = 0
pos_o = 0
neg_na = 0
neg_ra = 0
neg_o = 0
neu_na = 0
neu_ra = 0
neu_o = 0

#print(test_data)

for i in range(len(test_data)):
    if test_data["name"][i]=="narendra":
        if test_data["avg"][i]==1.0:
            pos_na+=1
        elif test_data["avg"][i]==0.5:
            neu_na+=1
        else:
            neg_na+=1
    elif test_data["name"][i]=="rahul":
        if test_data["avg"][i]==1.0:
            pos_ra+=1
        elif test_data["avg"][i]==0.5:
            neu_ra+=1
        else:
            neg_ra+=1
    else:
        if test_data["avg"][i]==1.0:
            pos_o+=1
        elif test_data["avg"][i]==0.5:
            neu_o+=1
        else:
            neg_o+=1
            
#print(pos_na,pos_ra,pos_o,neg_na,neg_ra,neg_o,neu_na,neu_ra,neu_o)
        
        