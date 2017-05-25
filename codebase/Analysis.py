from yahoo_finance import Share
from matplotlib import dates
import matplotlib.pyplot as pyplot


DB = Share('DANSKE.CO')

P = [[d['Date'],float(d['Close'])] for d in reversed(DB.get_historical('2017-01-01','2017-04-30'))]
Px = dates.datestr2num([x[0] for x in P])
Py = [y[1] for y in P]

print(Px[:10])
print(Py[:10])

pyplot.plot_date(Px,Py,'-')