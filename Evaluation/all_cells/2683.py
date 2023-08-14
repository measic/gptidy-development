import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.font_manager as font_manager
import matplotlib.dates as mdat

def make_date(month,year):
    date = dt.datetime(int(year), int(month), 1)
    out_date = mdat.date2num(date)
    return out_date

task_labels = []
task_labels.append('Literature review')
task_labels.append('Introduction to the latest version of the BaSTI code (Osservatorio Astronomico d''Abruzzo)')
task_labels.append('Submission of RD9R')
task_labels.append('Implementation of thermohaline mixing in the stellar evolution code, tests, comparisons with independent calculations, calibration of the diffusion efficiency coefficient')
task_labels.append('Implementation of rotation in the stellar evolution code')
task_labels.append('Write up and submit transfer report')
task_labels.append('Continuation of implementation of rotation, tests and comparisons with independent calculations')
task_labels.append('Calculation of models to study extended turn off phenomenon, comparison with observed CMDs, write up and submission paper about this study')
task_labels.append('Implementation of radiative levitation in the stellar evolution code, tests and comparisons with independent calculations')
task_labels.append('Calculation of models with rotation, levitation and thermohaline mixing for globular cluster turn off and horizontal branch stars. Comparisons with observations')
task_labels.append('Write up and submit two papers about this study')
task_labels.append('Write up and submit PhD thesis')
#Visit to Osservatorio Astronomico d''Abruzzo to be i

task_dates = []
task_dates.append([make_date(10,2017),make_date(12,2017)])
task_dates.append([make_date(11,2017),make_date(12,2017)])
task_dates.append([make_date(12,2017),make_date(2,2018)])
task_dates.append([make_date(2,2018),make_date(6,2018)])
task_dates.append([make_date(6,2018),make_date(9,2018)])
task_dates.append([make_date(6,2018),make_date(9,2018)])
task_dates.append([make_date(9,2018),make_date(2,2019)])
task_dates.append([make_date(2,2019),make_date(7,2019)])
task_dates.append([make_date(7,2019),make_date(12,2019)])
task_dates.append([make_date(12,2019),make_date(3,2020)])
task_dates.append([make_date(3,2020),make_date(5,2020)])
task_dates.append([make_date(4,2020),make_date(9,2020)])

print len(task_labels)
print len(task_dates)

plot_dates = {}
for i,j in enumerate(task_labels):
    plot_dates[j] = task_dates[i]
    
fig, ax = plt.subplots()
#ax = fig.add_subplot(111)

for i in range(len(task_labels)):
    start_date,end_date = plot_dates[task_labels[i]]
    ax.barh(i+1, end_date - start_date, left=start_date, height=0.3, align='center', color='blue',alpha = 0.75)
pos = np.arange(1,len(task_labels)+1,1)
locsy, labelsy = plt.yticks(pos,task_labels)
plt.setp(labelsy, fontsize = 10)

ax.axis('tight')
ax.set_ylim(ymin = 0.5, ymax = 12.5)
ax.grid(color = 'g', linestyle = ':')
 
ax.xaxis_date() #Tell matplotlib that these are dates...
 
rule = mdat.rrulewrapper(mdat.MONTHLY, interval=1)
loc = mdat.RRuleLocator(rule)
formatter = mdat.DateFormatter("%b '%y")
ax.invert_yaxis()
fig.autofmt_xdate()