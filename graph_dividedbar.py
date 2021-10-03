import numpy as np
import matplotlib.pyplot as plt
from name_avg import pos_na,pos_ra,pos_o,neg_na,neg_ra,neg_o,neu_na,neu_ra,neu_o

# set width of bar
barWidth = 0.25
#fig = plt.subplots(figsize =(12, 8))
# set height of bar
pos = [pos_na, pos_ra, pos_o]
neg = [neg_na, neg_ra, neg_o]
neu = [neu_na, neu_ra, neu_o]

# Set position of bar on X axis
br1 = np.arange(len(pos))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
plt.bar(br1, pos, color ='g', width = barWidth,
		edgecolor ='grey', label ='+ve')
plt.bar(br2, neg, color ='r', width = barWidth,
		edgecolor ='grey', label ='-ve')
plt.bar(br3, neu, color ='b', width = barWidth,
		edgecolor ='grey', label ='neutral')

# Adding Xticks
plt.xlabel('Canditates in Election', fontweight ='bold')
plt.ylabel('Count', fontweight ='bold')
plt.xticks([r + barWidth for r in range(len(pos))],
		['Narendra Modi', 'Rahul Gandhi', 'Others'])
plt.title("Vote distribution")
plt.legend()
plt.show()
