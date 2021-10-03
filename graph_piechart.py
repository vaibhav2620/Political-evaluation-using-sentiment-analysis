import matplotlib.pyplot as plt

from name_avg import pos_na,pos_ra,pos_o,neg_na,neg_ra,neg_o,neu_na,neu_ra,neu_o


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Narendra Modi', 'Rahul Gandhi', 'Others'
sizes = [pos_na+neg_ra+neu_na,pos_ra+neg_na+neu_ra,pos_o+neu_o+neg_o]
explode = (0.05, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Vote distribution")
plt.show()