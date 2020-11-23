#!usr/bin/env python
#
#<sixie6e@paracosmoclast>
#
#pseudolayout
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ezodf
#banks = pd.read_excel("/home/sixie6e/Documents/corporate_mapping/banks.xlsx")
banks = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/banks.ods")
nasdaq = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/nasdaq.ods")
djia = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/djia.ods")
crudeoil = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/crudeoil.ods")
snp500 = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/snp500.ods")
russell2000 = ezodf.opendoc("/home/sixie6e/Documents/corporate_mapping/russell2000.ods")
#print(snp500, nasdaq, djia, russell2000, crudeoil, banks)
labels = ['banks', 's&p500', 'nasdaq', 'djia', 'russell2000', 'crudeoil']
gross_rev = [0, 0, 0, 0, 0, 0]
net_rev = [233, 306, 2.54, 1.8, 1.67, 1.2]
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, gross_rev, width, label='gross')
rects2 = ax.bar(x + width/2, net_rev, width, label='net')
ax.set_ylabel('revenue in billions')
ax.set_title('revenue, stocks, banks')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()
