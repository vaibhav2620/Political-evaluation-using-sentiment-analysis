import matplotlib.pyplot as plt
import numpy as np

from name_avg import pos_na,pos_ra,pos_o,neg_na,neg_ra,neg_o,neu_na,neu_ra,neu_o



# create data
x = ['Narendra Modi', 'Rahul Gandhi', 'Others']
y1 = np.array([pos_na,pos_ra,pos_o])
y2 = np.array([neg_ra,neg_na,neg_o])
y3 = np.array([neu_na,neu_ra,neu_o])


# plot bars in stack manner
plt.bar(x, y1, color='g')
plt.bar(x, y2, bottom=y1, color='r')
plt.bar(x, y3, bottom=y1+y2, color='b')
plt.xlabel("Candidates in election", fontweight ='bold')
plt.ylabel("Votes(in %)", fontweight ='bold')
plt.legend(["+ve", "-ve of other", "Neutral"])
plt.title("Vote distribution")
plt.show()