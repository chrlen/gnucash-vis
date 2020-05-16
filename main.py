import pandas as pd
import numpy as np
import scipy as sp
import scipy.stats as sps
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/export", decimal=",")
for i in range(1, df.shape[0],2):
    df['Transaction ID'][i+1] = df['Transaction ID'][i]

idAndDate = df[['Date', 'Transaction ID']]
idToDate = {r[1][1]: r[1][0] for r in idAndDate.iterrows() if not pd.isna(r[1][1])}

for i in range(df.shape[0]):
    if pd.isna(df['Date'][i]):
        if idToDate.get(df['Transaction ID'][i]) != None:
            print("got id")
        else:
            print("no id")

df['Date'] = pd.to_datetime(df['Date'])
assetNames = set( [s for s in df['Full Account Name'].values if s.startswith("Asset")])
assets = df.loc[df['Full Account Name'].isin(assetNames) ]
expenseNames = set( [s for s in df['Full Account Name'].values if s.startswith("Expense")])
expenses = df.loc[df['Full Account Name'].isin(expenseNames) ]

assetSubset = assets[['Full Account Name', 'Amount Num.', 'Date']]
expenseSubset = expenses[['Account Name', 'Amount Num.', 'Date']]
for name in assetNames:
    x = assetSubset.loc[assetSubset['Full Account Name'] == name]['Date']
    y = assetSubset.loc[assetSubset['Full Account Name'] == name]['Amount Num.']
    #print(name)
    #print(x)
    plt.plot(x, y)
    
plt.show()
# plt.plot(assetSubset.loc[assetSubset['Account Name'] == 'Creditcard']['Amount Num.'])

#assets = df.loc[df['Full Account Name'].isin([
#    'Assets:Current Assets:Creditcard',
#    'Assets:Current Assets:Cash in Wallet',
#    'Assets:Current Assets:Checking Account',
#'Assets:Current Assets:Savings Account'
#])]
#
#
#['Amount Num.'].sum()
#df['Amount Num.'].sum()


#df.replace(r'\'0.00\'','0',regex=True)
#['Amount Num.'][0] = '0'
#df['Amount Num.'] = df['Amount Num.'].astype(np.float)
#pd.to_numeric(df['Amount Num.'], errors='coerce')

# file = "dataset/20200128_224212_gnucash_export_Book_1.gnca"

# tree = ET.parse(file)
# root = tree.getroot()
#for child in root:
##    print(child.tag, child.attrib)