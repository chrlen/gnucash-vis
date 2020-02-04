import pandas as pd
import numpy as np 
import scipy as sp
import scipy.stats as sps
import matplotlib.pyplot as plt


def cumDist(arr, rate =0.06):
    for i in range(len(arr)-1):
        arr[i+1] += arr[i]
        arr[i+1] += rate * arr[i]

    return arr

start='9/1/2020'
end='1/1/2058'

interest = 0.16
assets = 2000


ts = pd.date_range(start=start, end=end, freq='Y')
initialSalary = (50000 / 13) * 0.6666666666
save = initialSalary - 1000
init= [ initialSalary for i in ts]


init[0] += assets

value = cumDist(init.copy(), rate = interest)
income = cumDist(init.copy(),rate = 0)





df = pd.DataFrame({
    'date': ts,
    'value': value,
    'income': income
})

plt.plot(df['date'],df['value'])
plt.plot(df['date'], df['income'])

plt.show()